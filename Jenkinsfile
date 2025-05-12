pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                checkout([$class: 'GitSCM',
                  branches: [[name: '*/api']],
                  userRemoteConfigs: [[
                      url: 'https://github.com/lalit-shinkar/quotehub.git',
                      credentialsId: 'github-pat'
                  ]]
                ])
            }
        }

        stage('Set up Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t quotehub .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5000:5000 quotehub'
            }
        }
    }
}
