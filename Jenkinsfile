pipeline {
    agent {  label "master"    }
    stages {
        // Step 1
        stage('SCM') {
                steps {
                    git 'https://github.com/webdevprashant/Image-Classification-CNN.git'
                }        
        }
        // Step 2
        stage('Build Image') {
                steps {
                    sh 'docker build -t cnnmodelimg:$(BUILD_NUMBER)'
                }        
        }
        // Step 3
        stage('Train model') {
                steps {
                    sh 'docker run -dit cnnmodelimg:$(BUILD_NUMBER)' 
                }
        }
}
}