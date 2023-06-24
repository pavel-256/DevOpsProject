pipeline {
    agent any

    stages {
        stage('Pull code from GitHub') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: 'main']],
                    userRemoteConfigs: [[url: 'https://github.com/pavel-256/DevOpsProject.git']]
                ])
            }
        }

        stage('Install modules') {
            steps {
                script {
                    bat '''
                    py -m pip install flask
                    py -m pip install pymysql
                    py -m pip install selenium
                    py -m pip install requests
                    '''
                }
            }
        }

        stage('Run rest_app.py') {
            steps {
                script {
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
                bat 'py files/backend_testing.py'
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
                    dir('files') {
                        def envFile = readFile('.env')
                        def dockerHubUsername = envFile.readLines().find { it.startsWith('DOCKER_USERNAME=') }?.substring('DOCKER_USERNAME='.length())
                        def dockerHubPassword = envFile.readLines().find { it.startsWith('DOCKER_PASSWORD=') }?.substring('DOCKER_PASSWORD='.length())
                        def imageName = envFile.readLines().find { it.startsWith('IMAGE_NAME=') }?.substring('IMAGE_NAME='.length())

                        withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                            sh "docker login -u ${dockerHubUsername} -p ${dockerHubPassword}"
                            sh "docker push ${dockerHubUsername}/${imageName}"
                        }
                    }
                }
            }
        }

        stage('Set compose image version') {
            steps {
                sh 'echo "IMAGE_TAG=${BUILD_NUMBER}" > files/.env'
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
                    def imageName = readFile('files/.env').readLines().find { it.startsWith('IMAGE_NAME=') }?.substring('IMAGE_NAME='.length())
                    bat "docker-compose down"
                    bat "docker rmi ${imageName}"
                }
            }
        }
    }
}
