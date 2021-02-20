node()
{
    print "DEBUG: parameter foo = ${name}"
    print "DEBUG: parameter version = ${version}"
    print "DEBUG: parameter location = ${source}"
    print "DEBUG: parameter GOOGLE_SERVICE_ACCOUNT_KEY ${GOOGLE_SERVICE_ACCOUNT_KEY}"
    print "DEBUG: parameter GOOGLE_PROJECT_ID ${GOOGLE_PROJECT_ID}"


}
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                print "DEBUG: parameter build "
		script {
			  sh """
			  python --version
			  """
			}
            }
        }
        stage('Test') {
            steps {
                //
		  print "DEBUG: parameter test "


            }
        }
        stage('Deploy') {
            steps {
          		    print "DEBUG: parameter deploy "
          		    withCredentials([file(credentialsId: 'teanGCP', variable: 'FILE')]) {
                  checkout scm
          				sh """
          					#!/bin/bash
          					pip install python
                    echo "----------------------------------------- MINIO DOWNLOAD DONE ";
                    wget https://dl.min.io/client/mc/release/linux-amd64/mc
                    chmod +x mc
                    echo "----------------------------------------- minio connection ";

                    ./mc alias set minio http://172.21.0.5:9000 AKIAIOSFODNN7EXAMPLE wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
                    ./mc cp --recursive minio/mlflow/1/c987a6648b4845eab146f34eddd1ce96/artifacts/model .
                    ls;
          					echo "-----------------------------------------";

          				"""
				}
			}
            }
        }

}
