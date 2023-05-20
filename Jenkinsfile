
pipeline {
    agent any

//     stages {
//         stage('Pull Code') {
//             steps {
//                 // Pull code from your GitHub repository
//                   git url: 'https://github.com/pavel-256/DevOpsProject.git', branch: 'Dev_Branch'
//             }
//         }
        stage('Run Backend') {
            steps {
           bat 'start /min python rest_app.py'
       }

        }

        stage('Run Frontend') {
            steps {
                sh 'python web_app.py'
            }
        }

        stage('Run Backend Testing') {
            steps {
                sh 'python backend_testing.py'
            }
        }

        stage('Run Frontend Testing') {
            steps {
                sh 'python frontend_testing.py'
            }
        }

        stage('Run Combined Testing') {
            steps {
                sh 'python combined_testing.py'
            }
        }

        stage('Run Clean Environment') {
            steps {
                sh 'python clean_environment.py'
            }
        }
    }
}

