pipeline {
    agent any

    stages {
        stage('Build'){
            steps {
                echo 'Building...'
                sh ". ./venv/bin/activate && python --version"
            }
        }
        stage('Venv'){
        }
    }
}
