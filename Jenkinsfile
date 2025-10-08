pipeline {
    agent { label 'buit-in' }

    options {
        // Cancel previous build for the same PR
        disableConcurrentBuilds(abortPrevious: true)
    }

    environment {
        GIT_CREDENTIALS = 'ngrok_jenkins'
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Cloning repository and checking out branch ${env.BRANCH_NAME}"
                checkout([$class: 'GitSCM',
                          branches: [[name: "${env.BRANCH_NAME}"]],
                          doGenerateSubmoduleConfigurations: false,
                          extensions: [],
                          userRemoteConfigs: [[
                              url: 'https://github.com/jasanihardik/Playwright_Python_Framework.git',
                              credentialsId: "${env.GIT_CREDENTIALS}"
                          ]]
                ])
            }
        }

    stage('Print Info') {
        steps {
            script {
                echo "Branch: ${env.BRANCH_NAME}"
                if (env.CHANGE_ID) {
                    echo "PR #${env.CHANGE_ID} for branch ${env.CHANGE_TARGET}"
                }
                echo "Workspace: ${env.WORKSPACE}"
            }
        }
    }

}
