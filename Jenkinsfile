pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "dhaval1522/polling-app"
        KUBECONFIG = credentials('kubeconfig-cred') // Jenkins credential ID
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: "${env.BRANCH_NAME}", url: 'https://github.com/dhavalBhimani44/k8s-gitops-demo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE}:${BRANCH_NAME} ./app"
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    sh "docker push ${DOCKER_IMAGE}:${BRANCH_NAME}"
                }
            }
        }

        stage('Deploy to K8s') {
            steps {
                script {
                    if (BRANCH_NAME == 'dev') {
                        sh "kubectl apply -f k8s/dev/"
                    } else if (BRANCH_NAME == 'prod') {
                        sh "kubectl apply -f k8s/prod/"
                    } else {
                        echo 'Branch not configured for deployment.'
                    }
                }
            }
        }
    }
}
