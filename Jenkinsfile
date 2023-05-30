pipeline {
    agent any
    
    }
    stages {
       stage('Build') {
                steps {
                    echo 'Building ...'		   
            }
        }
       stage('List') {
                steps {
                    sh("dir ${JENKINS_HOME}")
            }
        }       
       stage('Test') {
                steps {
                    echo 'Testing...'
            }
        }
       stage('install requirements') {
            steps {                
                sh 'pip install -r requirements.txt'
            }
        }
        stage('run tests') {
            steps {
                sh 'pytest test_cases.py'
            }
        }
    }
}
