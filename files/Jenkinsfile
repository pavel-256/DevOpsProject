pipeline {
    agent any

    stages {
        stage('Pull Code') {
            steps {
                // Pull code from your Github repository
                git branch: 'main', url: 'https://github.com/pavel-256/DevOpsProject.git'
            }
        }

        stage('Install  modules') {
        // install modules
           steps {
                bat 'py -m pip install flask'
                bat 'py -m pip install pymysql'
                bat 'py -m pip install selenium'
            }
        }

        stage('Run rest_app.py') {
            // Step 2: Run rest_app.py (backend)
            steps {
                bat 'start /min python rest_app.py'
            }
        }

        stage('Run backend_testing.py') {
            // Step 3: Run backend_testing.py
            steps {
                bat 'python docker_backend_testing.py'
            }
        }

        stage('Run clean_environment.py') {
            // Step 4: Run clean_environment.py
            steps {
                bat 'python clean_environment.py'
            }
        }

        stage('Build Docker image') {
            // Step 5: Build Docker image locally
            steps {
                bat 'docker build -t your-image-name .'
            }
        }


stage('Push Docker image') {
    steps {
        script {
            // Read the Docker Hub credentials from the .env file
            def dockerHubUsername = readFile('.env').readLines().find { it.startsWith('DOCKER_USERNAME=') }?.substring('DOCKER_USERNAME='.length())
            def dockerHubPassword = readFile('.env').readLines().find { it.startsWith('DOCKER_PASSWORD=') }?.substring('DOCKER_PASSWORD='.length())

            // Login to Docker Hub and push the image
            withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                    def imageName = 'your-image-name'
                    def imageTag = env.BUILD_NUMBER
                    def dockerImage = docker.image("${imageName}:${imageTag}")

                    // Tag the image with the Docker Hub username and version
                    def taggedImage = "${dockerHubUsername}/${imageName}:${imageTag}"
                    dockerImage.tag(taggedImage)

                    // Push the tagged image to Docker Hub
                    dockerImage.push()
                }
            }
        }
    }
}


        stage('Set compose image version') {
            // Step 7: Set compose image version
            steps {
                bat 'echo IMAGE_TAG=%BUILD_NUMBER% > .env'
            }
        }

        stage('Run docker-compose up') {
            // Step 8: Run docker-compose up
            steps {
                bat 'docker-compose up -d'
            }
        }

        stage('Test dockerized app') {
            // Step 9: Test dockerized app using docker_backend_testing.py
            steps {
                bat 'python docker_backend_testing.py'
            }
        }

        stage('Clean environment') {
            // Step 10: Clean environment
            steps {
                bat 'docker-compose down'
                bat 'docker rmi your-image-name'
            }
        }
    }
}







