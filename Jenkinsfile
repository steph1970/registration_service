pipeline {
    agent any

    stages {
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
