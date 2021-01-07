pipeline {
    agent any

    stages {
        stage('Build'){
            steps {
                echo 'Create virtual environment...'
                sh """
                    virtualenv -p /usr/bin/python3 venv
                    . ./venv/bin/activate
                    python --version
                """
            }
        }
    }
}
