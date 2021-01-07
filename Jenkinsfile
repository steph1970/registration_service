pipeline {
    agent any

    stages {
        stage('Build'){
            steps {
                echo 'Building...'
                sh "virtualenv -p /usr/bin/pythpn3 venv && source ./venv/bin/activate && python --version"
            }
        }
    }
}
