pipeline {
    agent any

    environment {
        IMAGE_TAG = ""
    }

    stages {
        stage('Load .env file') {
            steps {
                script {
                    // Load the contents of the .env file into environment variables
                    def envFile = readFile('.env')
                    envFile.readLines().each { line ->
                        def (key, value) = line.tokenize('=')
                        env."${key.trim()}" = value.trim()
                    }
                }
            }
        }

        stage('Pull code from GitHub') {
            steps {
                git branch: 'main', url: 'https://github.com/pavel-256/DevOpsProject.git'
            }
        }

        stage('Install modules') {
            steps {
                bat 'py -m pip install flask'
                bat 'py -m pip install pymysql'
                bat 'py -m pip install selenium'
                bat 'py -m pip install requests'
            }
        }

        stage('Run rest_app.py') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'nohup python rest_app.py &'
                    } else {
                        bat 'start /B py rest_app.py'
                    }
                }
            }
        }

        stage('Run backend_testing.py') {
            steps {
                bat 'py docker_backend_testing.py'
            }
        }

        stage('Run clean_environment.py') {
            steps {
                bat 'py clean_environment.py'
            }
        }

        stage('Build Docker image') {
            steps {
                script {
                    def imageName = env.IMAGE_NAME
                    def imageTag = env.BUILD_NUMBER

                    // Tag the Docker image with the image tag
                    def taggedImage = "${imageName}:${imageTag}"

                    // Build the Docker image with the tagged image
                    bat "docker build -t ${taggedImage} ."

                    // Set the environment variable with the image tag for later use
                    env.IMAGE_TAG = imageTag
                }
            }
        }

        stage('Push Docker image') {
            steps {
                script {
                    def dockerHubUsername = env.DOCKER_USERNAME
                    def dockerHubPassword = env.DOCKER_PASSWORD
                    def imageName = env.IMAGE_NAME
                    def imageTag = env.IMAGE_TAG

                    def taggedImage = "${imageName}:${imageTag}"
                    def dockerHubImage = "${dockerHubUsername}/${imageName}:${imageTag}"

                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        bat "echo ${dockerHubPassword} | docker login -u ${dockerHubUsername} --password-stdin"
                        bat "docker tag ${taggedImage} ${dockerHubImage}"
                        bat "docker push ${dockerHubImage}"
                    }
                }
            }
        }

        stage('Set compose image version') {
            steps {
                sh "echo 'IMAGE_TAG=${env.IMAGE_TAG}' > .env"
            }
        }

        stage('Run docker-compose up') {
            steps {
                bat 'docker-compose up -d'
            }
        }

        stage('Test dockerized app') {
            steps {
                bat 'py docker_backend_testing.py'
            }
        }

        stage('Clean environment') {
            steps {
                script {
                    def imageName = env.IMAGE_NAME
                    def imageTag = env.IMAGE_TAG
                    def dockerHubUsername = env.DOCKER_USERNAME
                    def dockerHubImage = "${dockerHubUsername}/${imageName}:${imageTag}"

                    bat "docker-compose down"
                    bat "docker rmi ${dockerHubImage}"
                }
            }
        }
    }
}
