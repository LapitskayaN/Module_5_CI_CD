pipeline {
    agent any
    
    }
    stages {
       stage('Build') {
                steps {
                    echo 'Building ...'
		    echo "Running ${env.BUILD_ID} ${env.BUILD_DISPLAY_NAME} and JOB ${env.JOB_NAME}"
            }
        }
       stage('List') {
                steps {
                    sh("dir ${JENKINS_HOME}")
            }
        }       stage('Test') {
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
