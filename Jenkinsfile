pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/emreosminho/testAutomation1.git'
            }
        }

        stage('Set up Python Env') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh './venv/bin/python3 -m pytest tests/ --maxfail=1 --disable-warnings'
            }
        }
    }
}
