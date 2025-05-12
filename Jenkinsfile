pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/api']],  // Make sure this matches your working branch
                    doGenerateSubmoduleConfigurations: false,
                    extensions: [],
                    userRemoteConfigs: [[
                        url: 'https://github.com/lalit-shinkar/quotehub.git',
                        credentialsId: 'github-pat'  // Replace with your actual Jenkins GitHub PAT credentials ID
                    ]]
                ])
            }
        }

        stage('Install Requirements') {
            steps {
                sh 'pip install -r requirements.txt'
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
