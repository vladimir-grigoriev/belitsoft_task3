pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:latest'
                }
            }
            steps {
                sh 'python3 -m venv env'
                sh '. ./env/bin/activate '
                sh 'sudo pip install -r requirements.txt'
            }
        }
        stage('Test') { 
            agent {
                docker {
                    image 'qnib/pytest' 
                }
            }
            steps {
                sh 'pytest --junit-xml test-reports/results.xml tests/' 
            }
            post {
                always {
                    junit 'test-reports/results.xml' 
                }
            }
        }
    }
}