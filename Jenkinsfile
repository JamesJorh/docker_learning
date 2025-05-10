pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: 'github', // 你设置的 ID
                url: 'https://github.com/JamesJorh/docker_learning.git',
                branch: 'master'
            }
        }

        stage('Build') {
            steps {
                echo 'Running build...'
                // 构建逻辑
            }
        }
    }
}
