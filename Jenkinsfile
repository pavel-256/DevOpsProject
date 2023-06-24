pipeline {
    agent any

    stages {
        stage('Pull code from GitHub') {
            steps {
                // Pull code from your GitHub repository
                git branch: 'main', url: 'https://github.com/pavel-256/DevOpsProject.git'
            }
        }

        stage('Load .env file') {
            steps {
                script {
                    // Set the environment variables
                    env.IMAGE_TAG = '1.0.0'
                    env.DB_HOST = 'localhost'
                    env.DB_NAME = 'DevOps'
                    env.DB_USER = 'root'
                    env.DB_PASSWORD = ''
                    env.DB_ROOT_PASSWORD = ''
                    env.IMAGE_NAME = 'AmazingImage'
                    env.DOCKER_USERNAME = 'pavel256'
                    env.DOCKER_PASSWORD = 'L$t&caW?_t^vvu7'
                }
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
                    // Read the Docker Hub credentials from the .env file
                    def dockerHubUsername = env.DOCKER_USERNAME
                    def dockerHubPassword = env.DOCKER_PASSWORD

                    // Read the image name from the .env file
                    def imageName = env.IMAGE_NAME

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
                    def imageName = env.IMAGE_NAME
                    bat "docker-compose down"
                    bat "docker rmi ${imageName}"
                }
            }
        }
    }
}
