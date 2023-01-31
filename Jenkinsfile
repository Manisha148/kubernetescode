pipeline{
    environment {
    dockerhubb = 'https://registry.hub.docker.com'
    dockerhubCredential = 'dockerhub'
    dockerImage = ''
    SCANNER_HOME = tool 'sonar'
    //EMAIL_TO = 'manis@testingxperts.com'
  }
    agent any
    stages{
        stage('Clone repository') {
            steps{
                checkout scm
            }
        }

        stage('Build image') {
            steps{
                docker.build -t vishal7500/demo .
             }   
            }
    
  
       
   
    // stage('Test image') {
  

    //     app.inside {
    //         sh 'echo "Tests passed"'
    //     }
    // }

    stage('Push image') {
        steps{
            docker login -u vishal7500 -p Testing@123 && docker tag demo:latest vishal7500/demo:latest && docker push vishal7500/demo:latest
            }
            }
        }
    }
    stage('Sonarqube') {
      environment {
     scannerHome = tool 'sonar'
     }
    steps {
         withSonarQubeEnv('sonar') {
         sh "${scannerHome}/bin/sonar-scanner"
            }
         }
      }
   
     stage('Trigger ManifestUpdate') {
                echo "triggering ManifestUpdate"
                build job: 'ManifestUpdate', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
        }
     

// node {
//     def app

//     stage('Clone repository') {
      

//         checkout scm
//     }

//     stage('Build image') {
  
//        app = docker.build("vishal7500/demo")
//     }

//     stage('Test image') {
  

//         app.inside {
//             sh 'echo "Tests passed"'
//         }
//     }

//     stage('Push image') {
        
//         docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
//             app.push("${env.BUILD_NUMBER}")
//         }
//     }
//      stage('Sonarqube') {
//       environment {
//      scannerHome = tool 'sonar'
//      }
//     steps {
//          withSonarQubeEnv('sonar') {
//          sh "${scannerHome}/bin/sonar-scanner"
//             }
//          }
//       }
    
//     stage('Trigger ManifestUpdate') {
//                 echo "triggering updatemanifestjob"
//                 build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
//         }
// }
