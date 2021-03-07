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
                        echo "---------- START -------------------------------";

                        echo "----------------------------------------- MINIO DOWNLOAD OF THE MODEL";
                        wget https://dl.min.io/client/mc/release/linux-amd64/mc
                        chmod +x mc

                        ./mc alias set minio http://s3:9000 AKIAIOSFODNN7EXAMPLE wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
                        ./mc cp --recursive minio/mlflow/1/c987a6648b4845eab146f34eddd1ce96/artifacts/model .
                        echo "----------------------------------------- MODEL DOWNLOADED ";
                        ls
                        curl -o /tmp/google-cloud-sdk.tar.gz https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-225.0.0-linux-x86_64.tar.gz;
                		echo "-----------------------INSTALLING GCP DRIVER";
                		tar -xvf /tmp/google-cloud-sdk.tar.gz -C /tmp/;
                		/tmp/google-cloud-sdk/install.sh -q;

                		echo "----------------------------------------- DEPLOYING TO PROJECT";

                		/tmp/google-cloud-sdk/bin/gcloud config set project ${GOOGLE_PROJECT_ID};
                		/tmp/google-cloud-sdk/bin/gcloud auth activate-service-account --key-file ${FILE};

                		/tmp/google-cloud-sdk/bin/gcloud config list;
                		cd venv/bin
                		unlink venv/bin/python
                		unlink venv/bin/python3.9
                		unlink venv/bin/python3
                		ln -s  /usr/bin/python3 python3

                		/tmp/google-cloud-sdk/bin/gcloud app deploy -q;

                		echo "----------------------------------------- ALL DONE";
          				"""
				}
			}
            }
        }

}
