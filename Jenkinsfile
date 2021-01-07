pipeline {
    agent any

    stages {
        stage('Build'){
            steps {
                echo 'Create virtual environment...'
                sh "virtualenv -p /usr/bin/python3 venv"
                echo 'Activate virtual environment...'
                sh ". ./venv/bin/activate"
                echo 'Check...'
                sh "python --version"
            }
        }
    }
}
