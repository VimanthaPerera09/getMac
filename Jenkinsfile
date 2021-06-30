pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Built'
        bat(script: 'python getMac.py', returnStatus: true, returnStdout: true)
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
        sh 'jenkins/deploy.sh'
      }
    }

  }
}