pipeline {
    agent any
    stages {
        stage('Pull Code') {
            steps {
                // Pull code from your Github repository
                git branch: 'main', url: 'https://github.com/pavel-256/DevOpsProject.git'
            }
        }

        stage('Backend') {
            steps {
                // Run rest_app.py (backend)
                sh 'rest_app.py'
            }
        }

        stage('Frontend') {
            steps {
                // Run web_app.py (frontend)
                sh 'web_app.py'
            }
        }

        stage('Backend Testing') {
            steps {
                // Run backend_testing.py
                sh 'backend_testing.py'
            }
        }

        stage('Frontend Testing') {
            steps {
                // Run frontend_testing.py
                sh 'frontend_testing.py'
            }
        }

        stage('Combined Testing') {
            steps {
                // Run combined_testing.py
                sh 'combined_testing.py'
            }
        }

        stage('Clean Environment') {
            steps {
                // Run clean_environment.py
                sh 'clean_environment.py'
            }
        }
    }
}
