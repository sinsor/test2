pipeline {
  agent {
    docker {
      image 'sinsor/pytest:v1'
    }

  }
  stages {
    stage('build') {
      parallel {
        stage('build1') {
          steps {
            sh 'python --version'
            sh 'printenv'
          }
        }
        stage('build2') {
          steps {
            sh 'echo $TEST1'
          }
        }
      }
    }
    stage('test') {
      steps {
        sh 'python -m pytest --junitxml=build/reports/test-result.xml elma/test.py'
      }
    }
  }
  environment {
    TEST1 = 'true'
    TEST2 = 'sqlite'
  }
  post {
    always {
      echo 'This will always run'
      junit 'build/reports/*.xml'
      archiveArtifacts '*.txt'

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