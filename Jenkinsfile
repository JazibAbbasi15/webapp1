pipeline {
    agent { label 'ubuntu3' }

    environment {
        DOCKER_COMPOSE_CMD = 'docker-compose'
        REPO_URL = 'https://github.com/MUGHEESULHASSAN/Deploying_3_Tier_Web_App_Using_Docker_Compose_And_Jenkins_Pipeline.git'
        BRANCH = 'main'

        // Secure credentials injected from Jenkins Credentials
        MONGODB_URI = credentials('MONGODB_URI')
        CLOUDINARY_API_KEY = credentials('CLOUDINARY_API_KEY')
        CLOUDINARY_SECRET_KEY = credentials('CLOUDINARY_SECRET_KEY')
        CLOUDINARY_NAME = credentials('CLOUDINARY_NAME')
        JWT_SECRET = credentials('JWT_SECRET')
        ADMIN_EMAIL = credentials('ADMIN_EMAIL')
        ADMIN_PASSWORD = credentials('ADMIN_PASSWORD')
        CORS_ORIGIN = credentials('CORS_ORIGIN')
        VITE_BACKEND_URL = credentials('VITE_BACKEND_URL')
    }

    stages {

        // --- STAGE 1: Checkout Code ---
        stage('Checkout Code') {
            steps {
                echo "Cloning repository: ${env.REPO_URL}"
                git branch: env.BRANCH, url: env.REPO_URL
            }
        }

        // --- STAGE 2: Build and Run Containers ---
        stage('Build and Run Containers') {
            steps {
                script {
                    echo 'Stopping old containers...'
                    sh "${env.DOCKER_COMPOSE_CMD} down || true"

                    echo 'Running new containers with environment variables...'
                    sh """
                    MONGODB_URI='${MONGODB_URI}' \
                    CLOUDINARY_API_KEY='${CLOUDINARY_API_KEY}' \
                    CLOUDINARY_SECRET_KEY='${CLOUDINARY_SECRET_KEY}' \
                    CLOUDINARY_NAME='${CLOUDINARY_NAME}' \
                    JWT_SECRET='${JWT_SECRET}' \
                    ADMIN_EMAIL='${ADMIN_EMAIL}' \
                    ADMIN_PASSWORD='${ADMIN_PASSWORD}' \
                    CORS_ORIGIN='${CORS_ORIGIN}' \
                    VITE_BACKEND_URL='${VITE_BACKEND_URL}' \
                    ${env.DOCKER_COMPOSE_CMD} up -d --pull always
                    """
                }
            }
        }

        // --- STAGE 3: Verify Deployment ---
        stage('Verify Deployment') {
            steps {
                echo 'Checking running containers...'
                sh 'docker ps'

                // Optional health check example
                // sh 'curl -f http://localhost:8080 || (echo "App not responding!" && exit 1)'
            }
        }
    }

    // --- POST: Cleanup ---
    post {
        always {
            echo 'Cleaning up containers after build...'
            sh "${env.DOCKER_COMPOSE_CMD} down"
        }
    }
}
