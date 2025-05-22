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
                    docker.build("order-service", "./order-service")
                    docker.build("user-service", "./user-service")
                }
            }
        }

        stage('Login to ECR') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'aws-ecr-creds',
                        usernameVariable: 'AWS_ACCESS_KEY_ID',
                        passwordVariable: 'AWS_SECRET_ACCESS_KEY'
                    )
                ]) {
                    sh '''
                    export AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
                    export AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
                    export AWS_REGION=${AWS_REGION}

                    aws ecr get-login-password --region $AWS_REGION | \
                    docker login --username AWS --password-stdin $ECR_REGISTRY
                    '''
                }
            }
        }

        stage('Tag and Push Images') {
            steps {
                script {
                    // Tagging images
                    sh """
                    docker tag order-service:latest ${ORDER_REPO}:${IMAGE_TAG}
                    docker tag user-service:latest ${USER_REPO}:${IMAGE_TAG}
                    """

                    // Pushing to ECR
                    sh """
                    docker push ${ORDER_REPO}:${IMAGE_TAG}
                    docker push ${USER_REPO}:${IMAGE_TAG}
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
