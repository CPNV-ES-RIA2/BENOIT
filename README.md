# AwsImgToLabel 


## Description

This project is designed to convert an image to labels and the main features are upload an image to aws and get a sql file back filled with labels returned from aws's Rekognition model. With an user interface built with React to make the usage easier.

## Getting Started

### Prerequisites

List all dependencies and their version needed by the project as :

* Language : Python 3.11.6, React
* Package : boto3, dotenv, unittest
* AWS : IAM access configured with a bucket s3

### Configuration

Sensitive data like aws credentials, are stored in a .env file

## Deployment

### On dev environment

To get the dependencies you must install them with pip3.  
To run the tests, open a terminal at root of repo and write `python3 DataObjectTest.py` or `python3 LabelDetectorTest.py`.  
To run the sequence open a terminal at root of repo and write `python3 main.py`


## Directory structure

```
└── 📁RIA2
    └── .DS_Store
    └── .env.example
    └── .gitattributes
    └── .gitignore
    └── .gitignore.rtf
    └── 📁.vscode
        └── settings.json
    └── 📁APIGateway
        └── .DS_Store
        └── APIGatewayServer.py
        └── Dockerfile
        └── requirements.txt
    └── 📁LabelsDetection
        └── 📁DataObject
            └── AwsDataObjectImpl.py
            └── IDataObject.py
            └── 📁__pycache__
                └── AwsDataObjectImpl.cpython-311.pyc
                └── IDataObject.cpython-311.pyc
        └── DataObjectTest.py
        └── Dockerfile
        └── 📁LabelDetector
            └── .env
            └── AwsLabelDetectorImpl.py
            └── ILabelDetector.py
            └── RekognitionClient.py
            └── 📁__pycache__
                └── AwsLabelDetectorImpl.cpython-311.pyc
                └── ILabelDetector.cpython-311.pyc
                └── RekognitionClient.cpython-311.pyc
            └── image.png
            └── keys.json
        └── LabelDetectorTest.py
        └── LabelServer.py
        └── main.py
        └── requirements.txt
        └── 📁sql
        ├── tmp
    └── 📁Luncher
        └── api.sh
        └── frontend.sh
        └── frontend_pid.txt
        └── start.sh
        └── stop.sh
    └── 📁Ui
        └── .DS_Store
        └── 📁frontend
            └── .DS_Store
            └── .gitignore
            └── Dockerfile
            └── README.md
            └── 📁cypress
                └── .DS_Store
                └── 📁downloads
                └── 📁e2e
                    └── dragNdrop.cy.js
                    └── languages.cy.js
                    └── spec.cy.js
                └── 📁fixtures
                    └── Egger.jpeg
                    └── example.json
                └── 📁support
                    └── commands.js
                    └── e2e.js
            └── cypress.config.js
            └── default.conf
            └── 📁features
                └── detected_labels.feature
                └── drag_and_drop.feature
                └── load_language_by_global.feature
                └── local_language_change.feature
                └── 📁others
                    └── data_persistence.feature
                    └── display_request_pending.feature
                    └── dynamic_display_no_reload.feature
                    └── send_img_network_recovred.feature
                    └── upload_img_get_labels.feature
                └── parameters_adjustment.feature
            └── package-lock.json
            └── package.json
            └── 📁public
                └── favicon.ico
                └── index.html
                └── logo192.png
                └── logo512.png
                └── manifest.json
                └── robots.txt
            └── 📁src
                └── App.css
                └── App.js
                └── App.test.js
                └── 📁components
                    └── 📁container
                        └── index.jsx
                    └── 📁content
                        └── 📁image
                            └── index.jsx
                        └── 📁label
                            └── index.jsx
                └── index.css
                └── index.js
                └── logo.svg
                └── output.css
                └── reportWebVitals.js
                └── setupTests.js
                └── 📁translations
                    └── i18n.js
                    └── 📁locales
                        └── 📁de
                            └── translation.json
                        └── 📁en
                            └── translation.json
                        └── 📁fr
                            └── translation.json
            └── tailwind.config.js
    └── 📁docker
        └── 📁api-gateway
            └── dockerfile
        └── docker-compose.yml
        └── 📁python-backend
            └── dockerfile
        └── 📁view
            └── dockerfile
    └── docker-compose.yml
    └── docker-compose.yml.example
    └── 📁features
        └── 📁step_definitions
            └── react.js
    └── 📁tests
        └── async_aws_s3_operations.feature
        └── img_format_validation.feature
        └── network_error_managment.feature
        └── succesive_requests_support.feature
```

## Collaborate
To collaborate on the project, please read those documents first : 
*  (Branch Strategy)[https://github.com/BPTdev/RIA2/wiki/Branch-strategy]
*  (Commits Convention)[https://github.com/BPTdev/RIA2/wiki/Commits-Convention]
*  (Best Practices)[https://github.com/BPTdev/RIA2/wiki/Best-Practices#react]

## Run
To run the project you need to run 3 servers.
Please refer to this page (Local Development)[https://github.com/BPTdev/RIA2/wiki/Local-Development#introduction]

## License

* [glp-3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

## Contact

* Issue GitHub, Teams, Mail
