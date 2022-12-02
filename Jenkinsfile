pipeline {
  agent { docker { image 'python:3.10.0' } }
  stages{
    stages("build"){
      steps{
        sh 'pip install django'
      }
    }
    stages("test"){
      steps{
        sh 'python manage.py runserver'
      }
    }
    stages("deploy"){
      steps{
        echo "DEPLOYING NOW"
      }
    }
  }
}
