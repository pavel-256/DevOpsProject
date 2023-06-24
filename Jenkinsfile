
// check my jenkinsfiles

pipeline {
    agent any

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
                    def dockerfilePath = env.DOCKERFILE_PATH
                    bat "docker build -t ${imageName} ."
                }
            }
        }

//         stage('Push Docker image') {
//             steps {
//                 script {
//                     def dockerHubUsername = env.DOCKER_USERNAME
//                     def dockerHubPassword = env.DOCKER_PASSWORD
//                     def imageName = env.IMAGE_NAME
//
//                     withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
//                         bat "docker login -u ${dockerHubUsername} -p ${dockerHubPassword}"
//                         bat "docker tag ${imageName} ${dockerHubUsername}/${imageName}"
//                         bat "docker push ${dockerHubUsername}/${imageName}"
//                     }
//                 }
//             }
//         }

        stage('Set compose image version') {
            steps {
                bat 'echo "IMAGE_TAG=${BUILD_NUMBER}" > .env'
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
                    bat "docker-compose down"
                    bat "docker rmi ${imageName}"
                }
            }
        }
    }
}
