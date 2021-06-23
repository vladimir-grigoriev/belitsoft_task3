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
                sh 'pip install --upgrade pip'
                sh 'pip install selenium'
                sh 'pip install pytest'
            }
        }
        stage('Test') { 
            agent {
                docker {
                    image 'qnib/pytest' 
                }
            }
            steps {
                
                sh 'pytest tests/test_page2.py' 
            }
            post {
                always {
                    junit 'test-reports/results.xml' 
                }
            }
        }
    }
}