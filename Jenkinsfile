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
          					curl -O google-cloud-sdk.tar.gz https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-328.0.0-linux-x86.tar.gz
          					echo "-----------------------------------------";
                    ls
                    pwd
          					tar -xvf google-cloud-sdk.tar.gz ;
          					echo "-----------------------------------------";
          					./google-cloud-sdk/install.sh -q;
          					echo "-----------------------------------------";

          					echo "-----------------------------------------";
          				"""
				}
			}
            }
        }

}
