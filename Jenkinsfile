pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Built'
        bat(script: 'python getMac.py', returnStatus: true, returnStdout: true)
        input(message: 'Do you wish to build', ok: 'Yes')
      }
    }

    stage('Test') {
      steps {
        echo 'Testing'
      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploying'
      }
    }

  }
}