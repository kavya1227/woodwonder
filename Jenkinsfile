pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo '🔨 Building Docker image...'
                bat 'docker build -t woodwonder-app .'
            }
        }

        stage('Test') {
            steps {
                echo '🧪 Running tests (if any)...'
                // Replace with actual test command, or skip if not needed
                bat 'echo "No tests defined."'
            }
        }

        stage('Deploy') {
            steps {
                echo '🚀 Deploying Docker container...'
                // Stop and remove existing container if running
                bat '''
                docker stop woodwonder-container || echo "No running container"
                docker rm woodwonder-container || echo "No container to remove"
                docker run -d -p 8080:80 --name woodwonder-container woodwonder-app
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Deployment successful!'
        }
        failure {
            echo '❌ Deployment failed!'
        }
    }
}
