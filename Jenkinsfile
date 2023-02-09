pipeline {
  environment {
    dockerhubb = 'https://registry.hub.docker.com'
    dockerhubCredential = 'docker'
    dockerImage = ''
    SCANNER_HOME = tool 'SONAR'
    //EMAIL_TO = 'ravali.ganigapeta@testingxperts.com'
  }
agent any
  stages {
     stage('Cloning Git') {
      steps {
        git branch: 'main' ,  url: 'https://github.com/Manisha148/kubernetescode.git'
        }
     } 

 stage('Building image') {
   steps{
       script {
          sh 'docker build -t javaimg .'
          }
        }
      }


//  	stage('Push') {

// 		steps {
// 			sh 'docker push manishaverma/javaimg'
// 			}
// 		}
      
//    }
//  stage('Push Image') {
//       steps{
//         script {
//            sh 'docker.withRegistry(dockerhub, dockerhubCredential)' {
//           sh 'app.push("${env.BUILD_NUMBER}")'
       //sh 'curl "admin:ravali" -X PUT http://18.212.25.74:8001/repository/k8s-task/flask:8.0 '
        //flask:3.0.push("latest")
        
          //sh 'docker login -u ravali1505 -p Manoj@123@123'
//          sh 'docker login -u admin -p ravali 18.212.25.74:8001/repository/k8s-task/' 
//          sh 'docker push 18.212.25.74:8001/repository/k8s-task/flask:8.0'
//          sh 'docker logout http://18.212.25.74:8001/repository/k8s-task/'
      	stage('SonarQube analysis') {
    		
    		steps {
    			withSonarQubeEnv(credentialsId: 'SonarQubeToken', installationName: 'Production SonarQubeScanner') {
         			sh '''$SCANNER_HOME/bin/sonar-scanner \
         			-Dsonar.projectKey=SonarScanner \
         			-Dsonar.projectName=SonarScanner \
         			-Dsonar.projectVersion=${BUILD_NUMBER}-${GIT_COMMIT_SHORT}'''
       			}
     		}
  	}

       

    stage('slack notification') {
       steps{
          slackSend( channel: "#slacknotification", token: "fsYHGRDiC4X0FkEzdgLBQx0v", color: "good", message: "Test Email")  
           }
        }
    stage('selenium-test') {
      steps {
          sh 'mvn validate -P parallel'   
       }
     }
//   stage('Jmeter test report') {
//     steps {
//         sh 'jmeter -n -t /home/ubuntu/jmeter/bin/jenkins.jmx -l results.jtl'
//     }
//     }
    stage('Unit Testing') {
            steps{
                    perfReport filterRegex: '', showTrendGraphs: true, sourceDataFiles: '**/*.log'
            }
            post {
                success {
                    publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: './', reportFiles: 'index.html', reportName: 'HTML Report', reportTitles: '', useWrapperFileDirectly: true])
        }
      }
    }
//   stage('Email-Notification') {
//       steps {
//          emailext mimeType: 'text/html',               
//          subject: "[Jenkins]${currentBuild.fullDisplayName}",               
//          to:" vishalsadar75@gmail.com",             
//           body: """Please go to console output of ${BUILD_URL}input to approve or Reject"""    
//       input(id: 'Proceed1', message: 'Promote build?', parameters: [[$class: 'BooleanParameterDefinition', defaultValue: true, description: '', name: 'Please confirm you agree with this']])
//          sh 'docker build -t flask:8.0 .'
//              }
//           }
//   stage('Jmeter-test_reports') {
//       steps {
//         sh "/bin/python3 -m bzt.cli test.yml"
//       }
//    }
    
 
     stage('Trigger manifestupdate1') {
        steps {
                echo "triggering manifestupdate1"
                build job: 'manifestupdate1', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
        }
     }

  }
}
