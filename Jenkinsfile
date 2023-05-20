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
                sh 'python files/rest_app.py'
            }
        }

        stage('Frontend') {
            steps {
                // Run web_app.py (frontend)
                sh 'python files/web_app.py'
            }
        }

        stage('Backend Testing') {
            steps {
                // Run backend_testing.py
                sh 'python files/backend_testing.py'
            }
        }

        stage('Frontend Testing') {
            steps {
                // Run frontend_testing.py
                sh 'python files/frontend_testing.py'
            }
        }

        stage('Combined Testing') {
            steps {
                // Run combined_testing.py
                sh 'python files/combined_testing.py'
            }
        }

        stage('Clean Environment') {
            steps {
                // Run clean_environment.py
                sh 'python files/clean_environment.py'
            }
        }
    }
}
