pipeline {
    agent { docker { image 'python:3.5.1' } }

    environment {
        TEST1 = 'true'
        TEST2 = 'sqlite'
    }

    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'printenv'
            }
        }
        stage('test') {
            steps {
                sh 'python elma/test.py'
            }
        }
    }

    post {
        always {
            echo 'This will always run'
            junit 'build/reports/**/*.xml'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }

}
