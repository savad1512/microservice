pipeline {
    agent any

    environment {
        AWS_REGION = 'us-east-1'
        ECR_REGISTRY = '017820706788.dkr.ecr.us-east-1.amazonaws.com'
        ORDER_REPO = "${ECR_REGISTRY}/order-service"
        USER_REPO = "${ECR_REGISTRY}/user-service"
        IMAGE_TAG = "${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    docker.build("order-service", "./path/to/order-service")
                    docker.build("user-service", "./path/to/user-service")
                }
            }
        }

        stage('Login to ECR') {
            steps {
                script {
                    sh """
                    aws ecr get-login-password --region ${AWS_REGION} | \
                    docker login --username AWS --password-stdin ${ECR_REGISTRY}
                    """
                }
            }
        }

        stage('Tag and Push Images') {
            steps {
                script {
                    // Tagging images
                    sh """
                    docker tag order-service:latest ${ORDER_REPO}:latest
                    docker tag user-service:latest ${USER_REPO}:latest
                    """

                    // Pushing to ECR
                    sh """
                    docker push ${ORDER_REPO}:latest
                    docker push ${USER_REPO}:latest
                    """
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
