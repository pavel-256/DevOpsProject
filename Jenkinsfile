@Library('dotenv-library') _
import io.github.cdimascio.dotenv.Dotenv

pipeline {
    agent any

    stages {
        stage('Pull code from GitHub') {
            steps {
                // Pull code from your Github repository
                git branch: 'main', url: 'https://github.com/pavel-256/DevOpsProject.git'
            }
        }

        stage('Install modules') {
            steps {
                bat 'py -m pip install flask'
                bat 'py -m pip install pymysql'
                bat 'py -m pip install selenium'
                bat 'py -m pip install requests'
                bat 'py -m pip install python-dotenv'
            }
        }

        stage('Run rest_app.py') {
            steps {
                script {
                    // Start rest_app.py as a background process
                    if (isUnix()) {
                        sh 'nohup python rest_app.py &'
                    } else {
                        bat 'start /B py files/rest_app.py'
                    }
                }
            }
        }

        stage('Run backend_testing.py') {
            steps {
                bat 'py files/docker_backend_testing.py'
            }
        }

        stage('Run clean_environment.py') {
            steps {
                bat 'py files/clean_environment.py'
            }
        }

        stage('Push Docker image') {
            steps {
                script {
                    // Load variables from .env file
                    def dotenv = Dotenv.load()

                    // Read the Docker Hub credentials from the .env file
                    def dockerHubUsername = dotenv.get('DOCKER_USERNAME')
                    def dockerHubPassword = dotenv.get('DOCKER_PASSWORD')

                    // Read the image name from the .env file
                    def imageName = dotenv.get('IMAGE_NAME')

                    // Login to Docker Hub and push the image
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        bat "docker login -u ${dockerHubUsername} -p ${dockerHubPassword}"
                        bat "docker push ${dockerHubUsername}/${imageName}"
                    }
                }
            }
        }

        stage('Set compose image version') {
            steps {
                sh 'echo "IMAGE_TAG=${BUILD_NUMBER}" > .env'
            }
        }

        stage('Run docker-compose up') {
            steps {
                bat 'docker-compose up -d'
            }
        }

        stage('Test dockerized app') {
            steps {
                bat 'py files/docker_backend_testing.py'
            }
        }

        stage('Clean environment') {
            steps {
                script {
                    // Read the image name from the .env file
                    def dotenv = Dotenv.load()
                    def imageName = dotenv.get('IMAGE_NAME')

                    bat "docker-compose down"
                    bat "docker rmi ${imageName}"
                }
            }
        }
    }
}
