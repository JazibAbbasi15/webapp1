pipeline {
    agent { label 'ubuntu3' }

    environment {
        DOCKER_NETWORK = 'ci-network'
    }

    stages {

        stage('Clone Main Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Zillehuma626/ASSIGNMENT_3.git'
            }
        }

        stage('Build & Run Main Containers') {
            steps {
                sh '''
                sudo docker compose down || true
                sudo docker compose up -d --build
                '''
            }
        }

        stage('Verify Running Containers') {
            steps {
                sh 'sudo docker ps'
            }
        }

        stage('Wait for Frontend to Start') {
            steps {
                script {
                    sh '''
                    echo "Waiting for user-frontend-ci (5173) to be ready..."

                    while ! sudo docker run --rm --network=ci-network busybox nc -z user-frontend-ci 5173; do
                        echo "Frontend not ready... retrying..."
                        sleep 2
                    done

                    echo "Frontend is UP!"
                    '''
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                dir('selenium-tests') {
                    sh '''
                    echo "Building Selenium Test Image..."
                    sudo docker build -t selenium-tests .

                    echo "Running Selenium Tests..."
                    sudo docker run --rm \
                        --network=ci-network \
                        -e BASE_URL="http://user-frontend-ci:5173" \
                        selenium-tests
                    '''
                }
            }
        }

        stage('Show Logs') {
            steps {
                sh 'sudo docker compose logs --tail=100'
            }
        }
    }

    post {
        success {
            echo "✅ CI Build Completed Successfully!"
        }
        failure {
            echo "❌ Build Failed. Check logs."
        }
    }
}
