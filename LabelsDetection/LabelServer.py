from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import os
from werkzeug.utils import secure_filename
from DataObject.AwsDataObjectImpl import AwsDataObjectImpl
from LabelDetector.AwsLabelDetectorImpl import AwsLabelDetectorImpl

app = Flask(__name__)
CORS(app)

awsData = AwsDataObjectImpl()
awsLabel = AwsLabelDetectorImpl()

# Définir le dossier de téléchargement temporaire pour les fichiers uploadés
UPLOAD_FOLDER = 'tmp'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Définir les extensions de fichiers autorisées pour les images
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/analyze', methods=['POST'])
def analyze():
    print('Files in request:', request.files)
    # Vérifier si la requête contient un fichier
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']

    # Vérifier si un fichier a été sélectionné
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Vérifier si le fichier est une image
    if file and allowed_file(file.filename):
        # Enregistrer le fichier dans le dossier temporaire
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Save the labels params : 
        max_labels = request.form.get('max_labels', type=int)  # Provide default value if not found
        min_confidence = request.form.get('min_confidence', type=float)  # Provide default value if not found

        # Traiter l'image
        bucket = 'python.cloud.aws.edu'
        remote_full_path = f'{bucket}/{file_path}'
        remote_full_path = awsData.api_call(bucket, file_path, remote_full_path)
        tempUri = awsData.publish(remote_full_path)
        response = awsLabel.analyze(tempUri, max_labels, min_confidence)
        current_date = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        sql_file_name = f"sql/{filename}_{current_date}.sql"
        with open(sql_file_name, 'w') as sql_file:
            for label in response['Labels']:
                name = label['Name']
                confidence = label['Confidence']
                insert_statement = f"INSERT INTO your_table (name, confidence) VALUES ('{name}', {confidence});\n"
                sql_file.write(insert_statement)
        awsData.upload(sql_file_name, remote_full_path)

        # Supprimer le fichier temporaire après traitement
        os.remove(file_path)

        return response['Labels']

    return jsonify({"error": "Invalid file format"}), 400


if __name__ == '__main__':
    app.run(port=5171, debug=True)
