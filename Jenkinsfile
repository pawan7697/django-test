pipeline {
    agent any
    stages{
        stage("Clone code"){
            steps{
            echo "clone the code"
            git url: "https://github.com/pawan7697/django-test.git", branch: "main"
            }
        }
        stage("Build"){
            steps{
            echo "build the project"
            sh "docker build -t django-test ."
            }
        }
        stage("unit test"){
            steps{
          
            script {
                    docker.image("django-test:latest").inside {
                        sh 'python manage.py test'
                    }
                }
            }
        }
        stage("push"){
            steps{
            withCredentials([usernamePassword(credentialsId: 'jekins-test', usernameVariable: 'DockerHUbUser', passwordVariable: 'dockerHubPASSWORD')]){
                sh "docker tag django-test ${env.DockerHUbUser}/django-test:latest"
                sh "docker login -u ${env.DockerHUbUser} -p ${env.dockerHubPASSWORD}"
                sh "docker push ${env.DockerHUbUser}/django-test:latest"
                }
            }
        }
        stage("deploy"){
            steps{
                echo "Deploying the container"
                sh "docker-compose down && docker-compose up -d"
            }
        }
    }
    
    
}