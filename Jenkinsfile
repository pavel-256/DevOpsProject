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

//     stage('Run clean environment') {
//       steps {
//         bat 'py clean_environment.py'
//       }
//     }

    stage('Build Docker image') {
      steps {
        script {
          def imageName = env.IMAGE_NAME
          def imageTag = env.IMAGE_TAG

          bat "docker build -t ${imageName}:${imageTag} ."
        }
      }
    }

    stage('Set compose image version') {
      steps {
        bat "echo IMAGE_TAG=${env.IMAGE_TAG} > .env"
      }
    }

    stage('Run docker-compose up') {
      steps {
        bat 'docker-compose -f docker-compose.yml up -d --build'
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
        bat "docker image rmi ${env.IMAGE_NAME}:${env.IMAGE_TAG}"
      }
    }

    stage('Deploy HELM chart') {
      steps {
          bat 'helm install flaskchart flaskchart'
          bat "helm upgrade --install flaskchart flaskchart --set image.version=${imageTag}"
          bat "sed -i 's/version: \"[0-9]*\"/version: ${imageTag}/' flaskchart/values.yaml"
          bat 'helm upgrade --install flaskchart flaskchart -f flaskchart/values.yaml'
      }
    }

    stage('Write service URL into k8s_url.txt') {
      steps {
        bat 'minikube service flaskchart --url >k8s_url.txt'
      }
    }

    stage('Test deployed app') {
      steps {
        bat 'py K8S_backend_testing.py'
      }
    }

    stage('Clean HELM environment') {
      steps {
        bat 'helm delete flaskchart '
      }
    }
  }
}
