pipeline {
    agent any

    stages {
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

        stage('Load .env file') {
            steps {
                script {
                    withEnv(["ENV_FILE=.env"]) {
                        sh 'source $ENV_FILE'
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
                    def imageName = readFile('.env').readLines().find { it.startsWith('IMAGE_NAME=') }?.substring('IMAGE_NAME='.length())
                    bat "docker-compose down"
                    bat "docker rmi ${imageName}"
                }
            }
        }
    }
}
