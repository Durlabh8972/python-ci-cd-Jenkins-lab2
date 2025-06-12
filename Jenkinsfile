pipeline {
    agent any

    tools {
        python 'Python3'
    }

    environment {
        EMAIL_RECIPIENT = 'your-college-email@example.com'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/your-username/python-ci-cd-lab.git'
            }
        }

        stage('Setup Python') {
            steps {
                sh 'python --version'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                echo 'Simulating Build Process'
                sh 'echo "Build completed successfully!"'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'pytest test_app.py'
            }
        }

        stage('Notify') {
            steps {
                mail to: "${EMAIL_RECIPIENT}",
                     subject: "Jenkins Job - Build Success: ${env.JOB_NAME} [#${env.BUILD_NUMBER}]",
                     body: "Good news! The build passed all stages. ✔️"
            }
        }
    }

    post {
        failure {
            mail to: "${EMAIL_RECIPIENT}",
                 subject: "Jenkins Job - Build Failed: ${env.JOB_NAME} [#${env.BUILD_NUMBER}]",
                 body: "Something went wrong. ❌ Please check the Jenkins console output."
        }
    }
}
