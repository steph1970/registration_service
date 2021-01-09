pipeline {
    agent any

    stages {
        stage ('Build/Publish Docker Image'){
            steps {
                script {
                    def branch = env.GIT_BRANCH
                    def b = branch.replaceAll('origin/', '')
                    println b
                }
            }
        }
        stage('Build'){
            steps {
                echo 'Create virtual environment...'
                 sh script: $/
                    sed 's/origin\/main/main/' <<< ${GIT_BRANCH}
                    virtualenv -p /usr/bin/python3 venv
                    . ./venv/bin/activate
                    python --version
                /$
            }
        }
    }
}
