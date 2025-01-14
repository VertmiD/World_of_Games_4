pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "your-dockerhub-username/your-repository-name:latest" // Update with your DockerHub username and repository
        CONTAINER_NAME = "test-container"
        TEST_FILE = "e2e.py" // Ensure this file exists in your repo
        MOUNT_FILE = "Scores.txt" // Ensure this file exists in your repo
    }
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the repository...'
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Building the Docker image...'
                sh """
                docker build -t $DOCKER_IMAGE .
                """
            }
        }
        stage('Run') {
            steps {
                echo 'Running the Docker container...'
                sh """
                docker run -d --rm --name $CONTAINER_NAME -p 8777:8777 -v $WORKSPACE/$MOUNT_FILE:/app/$MOUNT_FILE $DOCKER_IMAGE
                """
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh """
                python3 $TEST_FILE || exit 1
                """
            }
        }
        stage('Finalize') {
            steps {
                echo 'Stopping the container and pushing the image...'
                sh """
                docker stop $CONTAINER_NAME
                docker push $DOCKER_IMAGE
                """
            }
        }
    }
    post {
        always {
            echo 'Cleaning up...'
            sh """
            docker stop $CONTAINER_NAME || true
            docker rm $CONTAINER_NAME || true
            """
        }
        failure {
            echo 'Build failed!'
        }
        success {
            echo 'Build succeeded!'
        }
    }
}
