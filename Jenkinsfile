pipeline {
    agent any
    
    stages {
       stage('Build') {
                steps {
            		sh 'python3 -m pip install pytest'
		            sh 'pip install pytest-html'
		            sh 'pip install pymssql'	   
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
                sh 'pip install pytest'
                sh 'pip install pymssql'
            }
        }
        stage('run tests') {
            steps {
                sh 'pytest test_cases.py' 
            }
        }
       stage('create report') {
            steps {                
                sh 'pytest --html=report.html'
            }
        }        
    }
}
