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
                bat 'echo "No tests defined."'
            }
        }

        stage('Deploy') {
            steps {
                echo '🚀 Deploying Docker container...'
                bat '''
                    docker stop woodwonder-container || echo "No running container"
                    docker rm woodwonder-container || echo "No container to remove"
                    docker run -d -p 8082:8000 --name woodwonder-container woodwonder-app
                '''
            }
        }
    }

    post {
        success {
            mail to: '2200031107@kluniversity.in',
                 subject: "Deployment Success - Woodwonder",
                 body: "✅ Jenkins has successfully deployed your application!"
        }
        failure {
            mail to: '2200031107@kluniversity.in',
                 subject: "Deployment Failed - Woodwonder",
                 body: "❌ Jenkins failed to deploy your app. Check the logs."
        }
    }
}
