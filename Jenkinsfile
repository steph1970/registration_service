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
                    
                    def build_str  = "docker build -t svanerp/registration_service:" + branch + " ."
                    build = build_str.execute()
                    build.waitForOrKill(5000)
                    
                    def login = "docker login -u credentials('DOCKER_HUB_USERNAME') -p credentials('DOCKER_HUB_PASSWORD')".execute()
                    login.waitForOrKill(1000)
                    
                    def push_str = "docker push svanerp/registration_service:" + branch
                    push = push_str.execute()
                    push.waitForOrKill(5000)
                }
            }
        }
    }
}
