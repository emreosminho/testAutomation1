pipeline {
    agent any

    stages {
        stage('Ortamı Hazırla') {
            steps {
                bat '''
                    python -m venv venv
                    venv\\Scripts\\activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Testleri Çalıştır') {
            steps {
                bat '''
                    venv\\Scripts\\activate
                    pytest tests\\ --html=rapor.html
                '''
            }
        }

        stage('Test Raporunu Yayınla') {
            steps {
                publishHTML([
                    reportDir: '.',
                    reportFiles: 'rapor.html',
                    reportName: 'Selenium Test Raporu'
                ])
            }
        }
    }
}
