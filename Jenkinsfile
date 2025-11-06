pipeline {
    agent any

    environment {
        KUBECONFIG = credentials('kubeconfig-cred-id')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build & Push Image') {
            steps {
                script {
                    sh '''
                    docker build -t polling-app:${GIT_COMMIT} ./polling-app
                    docker tag polling-app:${GIT_COMMIT} myrepo/polling-app:${GIT_BRANCH}
                    docker push myrepo/polling-app:${GIT_BRANCH}
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    if (env.GIT_BRANCH == 'origin/dev') {
                        sh 'kubectl apply -f k8s/dev/'
                    } else if (env.GIT_BRANCH == 'origin/prod') {
                        sh 'kubectl apply -f k8s/prod/'
                    } else {
                        echo "Branch not recognized for deployment"
                    }
                }
            }
        }
    }

    post {
        success {
            echo "Deployment successful for branch ${GIT_BRANCH}"
        }
        failure {
            echo "Deployment failed!"
        }
    }
}
