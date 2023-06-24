pipeline {
    agent any

    stages {
        stage('Pull code from GitHub') {
            steps {
                // Pull code from your GitHub repository
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

        stage('Load environment variables') {
            steps {
                script {
                    // Load environment variables from .env file
                    bat 'py -c "from dotenv import load_dotenv; load_dotenv()"'
                }
            }
        }

        stage('Run rest_app.py') {
            steps {
                script {
                    // Start rest_app.py as a background process
                    if (isUnix()) {
                        sh 'nohup python files/rest_app.py &'
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
                    // Read the Docker Hub credentials from the .env file
                    def dockerHubUsername = bat(script: 'py -c "from dotenv import load_dotenv; load_dotenv(); import os; print(os.getenv(\'DOCKER_USERNAME\'))"', returnStdout: true).trim()
                    def dockerHubPassword = bat(script: 'py -c "from dotenv import load_dotenv; load_dotenv(); import os; print(os.getenv(\'DOCKER_PASSWORD\'))"', returnStdout: true).trim()
                    def imageName = bat(script: 'py -c "from dotenv import load_dotenv; load_dotenv(); import os; print(os.getenv(\'IMAGE_NAME\'))"', returnStdout: true).trim()

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
                    def imageName = bat(script: 'py -c "from dotenv import load_dotenv; load_dotenv(); import os; print(os.getenv(\'IMAGE_NAME\'))"', returnStdout: true).trim()
                    bat "docker-compose down"
                    bat "docker rmi ${imageName}"
                }
            }
        }
    }
}
