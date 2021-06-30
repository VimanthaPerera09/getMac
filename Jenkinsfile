pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Built'
        sh 'python getMac.py'
      }
    }

    stage('Test') {
      steps {
        echo 'Testing'
        sh 'jenkins/test-all.sh'
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