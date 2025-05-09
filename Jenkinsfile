pipeline {
    agent {
        docker {
            image 'docker:20.10.16'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    
    environment {
        // 修改为您的DockerHub用户名
        DOCKER_HUB_USERNAME = 'xiatiantian44'
        // 修改为您希望的镜像名称
        IMAGE_NAME = 'docker_learning'
        // 容器名称
        CONTAINER_NAME = 'docker_learning_container'
        // 容器运行的端口映射，根据您的应用需求修改
        CONTAINER_PORT = '8080:8080'
    }
    
    stages {
        stage('Clone Repository') {
            steps {
                // 清理工作区
                cleanWs()
                // 克隆代码
                git 'https://github.com/JamesJorh/docker_learning.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // 构建Docker镜像
                    sh "docker build -t ${DOCKER_HUB_USERNAME}/${IMAGE_NAME}:latest ."
                }
            }
        }
        
        stage('Push to DockerHub') {
            steps {
                script {
                    // 使用之前设置的凭证登录DockerHub
                    withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        sh "echo ${DOCKER_PASSWORD} | docker login -u ${DOCKER_USERNAME} --password-stdin"
                        // 推送镜像到DockerHub
                        sh "docker push ${DOCKER_HUB_USERNAME}/${IMAGE_NAME}:latest"
                    }
                }
            }
        }
        
        stage('Deploy Container') {
            steps {
                script {
                    // 停止并删除旧容器（如果存在）
                    sh "docker stop ${CONTAINER_NAME} || true"
                    sh "docker rm ${CONTAINER_NAME} || true"
                    
                    // 运行新容器
                    sh "docker run -d -p ${CONTAINER_PORT} --name ${CONTAINER_NAME} ${DOCKER_HUB_USERNAME}/${IMAGE_NAME}:latest"
                }
            }
        }
    }
    
    post {
        always {
            // 清理工作，确保登出DockerHub
            sh "docker logout || true"
        }
    }
}
