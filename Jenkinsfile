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
                    export PYTHONPATH=$PYTHONPATH:.
                    python -m unittest tests/test_submission.py
                 """
            }
        }
        stage ('Build/Publish Docker Image'){
            steps {
                script {
                    def branch = (env.GIT_BRANCH).replaceAll('origin/', '')
                    println branch
                    def sout = new StringBuilder(), serr = new StringBuilder()
                    
                    def build  = 'docker build -t svanerp/registration_service:${GIT_COMMIT} .'.execute()
                    build.consumeProcessOutput(sout, serr)
                    build.waitForOrKill(1000)
                    println "out> $sout\nerr> $serr"
                    
                    def login = "docker login -u credentials('DOCKER_HUB_USERNAME') -p credentials('DOCKER_HUB_PASSWORD')"
                    login.consumeProcessOutput(sout, serr)
                    login.waitForOrKill(1000)
                    println "out> $sout\nerr> $serr
                    
                    def push = 'docker push svanerp/registration_service:' + branch
                    push.consumeProcessOutput(sout, serr)
                    push.waitForOrKill(1000)
                    println "out> $sout\nerr> $serr
                }
            }
        }
    }
}
