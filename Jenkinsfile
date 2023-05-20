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
                bat 'py files/rest_app.py'
            }
        }

        stage('Frontend') {
            steps {
                // Run web_app.py (frontend)
                bat 'py files/web_app.py'
            }
        }

        stage('Backend Testing') {
            steps {
                // Run backend_testing.py
                bat 'py files/backend_testing.py'
            }
        }

        stage('Frontend Testing') {
            steps {
                // Run frontend_testing.py
                bat 'py files/frontend_testing.py'
            }
        }

        stage('Combined Testing') {
            steps {
                // Run combined_testing.py
                bat 'py files/combined_testing.py'
            }
        }

        stage('Clean Environment') {
            steps {
                // Run clean_environment.py
                bat 'py files/clean_environment.py'
            }
        }
    }
}
