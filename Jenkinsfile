pipeline {
    agent any

    environment {
        IMAGE_TAG = '1.0.0'
        DB_HOST = 'localhost'
        DB_NAME = 'DevOps'
        DB_USER = 'root'
        DB_PASSWORD = ''
        DB_ROOT_PASSWORD = ''
        IMAGE_NAME = 'AmazingImage'
        DOCKER_USERNAME = 'Pavel256'
        DOCKER_PASSWORD = 'L$t&caW?_t^vvu7'
    }

    stages {
        stage('Pull code from GitHub') {
            steps {
                // Pull code from your GitHub repository
                git branch: 'main', url: 'https://github.com/pavel-256/DevOpsProject.git'
            }
        }

        stage('Install modules') {
            steps {
                sh 'pip install flask'
                sh 'pip install pymysql'
                sh 'pip install selenium'
                sh 'pip install requests'
                sh 'pip install python-dotenv'
            }
        }

        stage('Run rest_app.py') {
            steps {
                script {
                    // Start rest_app.py as a background process
                    sh 'nohup python rest_app.py &'
                }
            }
        }

        stage('Run backend_testing.py') {
            steps {
                sh 'python docker_backend_testing.py'
            }
        }

        stage('Run clean_environment.py') {
            steps {
                sh 'python clean_environment.py'
            }
        }

        stage('Push Docker image') {
            steps {
                script {
                    // Login to Docker Hub and push the image
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh "docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}"
                        sh "docker push ${DOCKER_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}"
                    }
                }
            }
        }

        stage('Set compose image version') {
            steps {
                sh "echo 'IMAGE_TAG=${BUILD_NUMBER}' > .env"
            }
        }

        stage('Run docker-compose up') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Test dockerized app') {
            steps {
                sh 'python docker_backend_testing.py'
            }
        }

        stage('Clean environment') {
            steps {
                sh 'docker-compose down'
                sh 'docker rmi ${DOCKER_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}'
            }
        }
    }
}
