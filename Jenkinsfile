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
            }
        }

        stage('Run rest_app.py') {
            steps {
                script {
                    // Start rest_app.py as a background process
                    if (isUnix()) {
                        sh 'nohup python rest_app.py &'
                    } else {
                        bat 'start /B python files/rest_app.py'
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
                    def dockerHubUsername = readFile('.env').readLines().find { it.startsWith('DOCKER_USERNAME=') }?.substring('DOCKER_USERNAME='.length())
                    def dockerHubPassword = readFile('.env').readLines().find { it.startsWith('DOCKER_PASSWORD=') }?.substring('DOCKER_PASSWORD='.length())

                    // Read the image name from the .env file
                    def imageName = readFile('.env').readLines().find { it.startsWith('IMAGE_NAME=') }?.substring('IMAGE_NAME='.length())

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
                    def imageName = readFile('.env').readLines().find { it.startsWith('IMAGE_NAME=') }?.substring('IMAGE_NAME='.length())
                    bat "docker-compose down"
                    bat "docker rmi ${imageName}"
                }
            }
        }
    }
}
