pipeline {
    agent any

    stages {   
        stage('Tests'){
            steps {
                echo 'Create virtual environment and launch tests...'
                sh """
                    virtualenv -p /usr/bin/python3 venv
                    . ./venv/bin/activate
                    python --version
                    pip install -r requirements.txt
                    
                 """
            }
        }
        stage ('Build/Publish Docker Image'){
            steps {
                script {
                    def branch = (env.GIT_BRANCH).replaceAll('origin/', '')
                    println branch
                    
                    def build  = 'docker build -t svanerp/registration_service:${GIT_COMMIT} .'.execute()
                    build.waitForOrKill(5000)
                    
                    def login = "docker login -u credentials('DOCKER_HUB_USERNAME') -p credentials('DOCKER_HUB_PASSWORD')"
                    login.waitForOrKill(1000)
                    
                    def push = "docker push svanerp/registration_service:" + branch
                    push.waitForOrKill(5000)
                }
            }
        }
    }
}
