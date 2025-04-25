pipeline {
    agent any

    environment {
        IMAGE_TAG = "latest"
    }

    stages {
        stage('Build') {
            steps {
                script {
                    echo "Building Docker images..."
                    sh 'docker build -t ecommerce-backend ./backend'
                    sh 'docker build -t ecommerce-frontend ./frontend'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo "Running tests..."
                    sh 'docker run --rm ecommerce-backend npm test'  // Modify based on your backend stack
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo "Deploying to Kubernetes..."
                    sh 'kubectl apply -f k8s/' // assumes you have k8s manifests in a "k8s" folder
                }
            }
        }
    }

    post {
        failure {
            echo 'Build failed!'
        }
        success {
            echo 'Build and deploy succeeded!'
        }
    }
}
