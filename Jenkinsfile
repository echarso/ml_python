node()
{
    print "DEBUG: parameter foo = ${name}"
    print "DEBUG: parameter version = ${version}"
    print "DEBUG: parameter location = ${source}"
    print "DEBUG: parameter GOOGLE_SERVICE_ACCOUNT_KEY ${GOOGLE_SERVICE_ACCOUNT_KEY}"
    print "DEBUG: parameter GOOGLE_PROJECT_ID ${GOOGLE_PROJECT_ID}"
    print "DEBUG: parameter service-name ${service-name}"



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
                          rm conf.txt
                          echo ${name}, >> conf.txt
                          echo ${version}, >> conf.txt
                          echo ${source}  >> conf.txt
                          echo service: ${service-name}>> app.yaml
                          cat conf.txt
                          cat app.yaml
                          ls
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
                        ./mc cp --recursive ${source} .
                        echo "----------------------------------------- MODEL DOWNLOADED ";
                        ls
                        ls model/
                        rm mc*
                        curl -o /tmp/google-cloud-sdk.tar.gz https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-225.0.0-linux-x86_64.tar.gz;
                		echo "-----------------------INSTALLING GCP DRIVER";
                		tar -xvf /tmp/google-cloud-sdk.tar.gz -C /tmp/;
                		/tmp/google-cloud-sdk/install.sh -q;

                		echo "----------------------------------------- DEPLOYING TO PROJECT";

                		/tmp/google-cloud-sdk/bin/gcloud config set project ${GOOGLE_PROJECT_ID};
                		/tmp/google-cloud-sdk/bin/gcloud auth activate-service-account --key-file ${FILE};

                		/tmp/google-cloud-sdk/bin/gcloud config list;
                		ls venv/bin
                		unlink venv/bin/python
                		unlink venv/bin/python3.9
                		unlink venv/bin/python3
                		cd venv/bin

                		ln -s  /usr/bin/python3 python3
                        cd ../..
                		/tmp/google-cloud-sdk/bin/gcloud app deploy -q;

                		echo "----------------------------------------- ALL DONE";
          				"""
				}
			}
            }
        }

}
