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

    stage('Run backend') {
      steps {
        script {
          if (isUnix()) {
            sh 'nohup python rest_app.py &'
          } else {
            bat 'start /min py rest_app.py'
          }
        }
      }
    }

    stage('Run backend testing') {
      steps {
        bat 'py backend_testing.py'
      }
    }

    stage('Run clean environment') {
      steps {
        bat 'py clean_environment.py'
      }
    }

    stage('Build Docker image') {
      steps {
        script {
          def imageName = env.IMAGE_NAME

          bat "docker build -t ${imageName}  ."
        }
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

          // Tag the image with the build number
          def taggedImage = "${imageName}:${env.IMAGE_TAG}"

          // Login to Docker Hub and push the image
          withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
            bat "docker login -u ${dockerHubUsername} -p ${dockerHubPassword}"
            bat "docker tag ${imageName} ${dockerHubUsername}/${taggedImage}"
            bat "docker push ${dockerHubUsername}/${taggedImage}"
          }
        }
      }
    }

    stage('Set compose image version') {
      steps {
        bat 'echo IMAGE_TAG=${BUILD_NUMBER} > .env'
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

    stage('Clean compose environment') {
      steps {
        bat 'docker-compose down'
        bat 'docker rmi ${env.IMAGE_NAME}:${env.IMAGE_TAG}'
      }
    }

    stage('Deploy HELM chart') {
      steps {
        bat "helm upgrade --install test ./chart --set image.version=${env.DOCKER_USERNAME}:${env.IMAGE_TAG}"
      }
    }

    stage('Write service URL into k8s_url.txt') {
      steps {
        bat 'minikube service hello-python-service --url > k8s_url.txt'
      }
    }

    stage('Test deployed app') {
      steps {
        bat 'py K8S_backend_testing.py'
      }
    }

    stage('Clean HELM environment') {
      steps {
        bat 'helm delete test --purge'
      }
    }
  }
}
