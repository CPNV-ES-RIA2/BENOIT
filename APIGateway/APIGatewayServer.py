from flask import Flask, request, jsonify
from flask_cors import CORS

import requests

app = Flask(__name__)
CORS(app)


@app.route('/api/analyze', methods=['POST'])
def analyze_image():
    if 'image' in request.files:
        image = request.files['image']
        if image.filename != '':
            # Prepare the file and data for the multipart request
            files = {
                'file': (image.filename, image, 'image/jpeg')
            }
            data = {
                'max_labels': request.form.get('max_labels'),
                'min_confidence': request.form.get('min_confidence')
            }
            # Make the HTTP POST request
            response = requests.post('http://localhost:5171/analyze', files=files, data=data)
            return jsonify(response.json())
        else:
            return jsonify({'error': 'No valid image provided'}), 400
    else:
        return jsonify({'error': 'No image file part'}), 400


if __name__ == '__main__':
    app.run(port=5170, debug=True)
