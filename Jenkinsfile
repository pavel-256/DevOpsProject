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
                bat 'git clone -b main https://github.com/pavel-256/DevOpsProject.git files'
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
                bat 'start /B py files/rest_app.py'
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
                bat """
                echo DOCKER_USERNAME=${DOCKER_USERNAME} > files/.env
                echo DOCKER_PASSWORD=${DOCKER_PASSWORD} >> files/.env
                echo IMAGE_NAME=${IMAGE_NAME} >> files/.env
                docker login -u %DOCKER_USERNAME% -p %DOCKER_PASSWORD%
                docker push %DOCKER_USERNAME%/%IMAGE_NAME%
                """
            }
        }

        stage('Set compose image version') {
            steps {
                bat "echo IMAGE_TAG=${BUILD_NUMBER} > files/.env"
            }
        }

        stage('Run docker-compose up') {
            steps {
                bat 'docker-compose -f files/docker-compose.yml up -d'
            }
        }

        stage('Test dockerized app') {
            steps {
                bat 'py files/docker_backend_testing.py'
            }
        }

        stage('Clean environment') {
            steps {
                bat """
                docker-compose -f files/docker-compose.yml down
                docker rmi %IMAGE_NAME%
                """
            }
        }
    }
}
