pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                dir("${env.WORKSPACE}/outer-loop-cli") {
                    sh '''
                    python3 -m venv ./venv
                    . ./venv/bin/activate
                    ./venv/bin/pip install -r src/requirements.txt
                    ./venv/bin/pip install --editable ./src
                    '''
                    
                    withCredentials([
                        file(credentialsId: 'GOOGLE_APPLICATION_CREDENTIALS', variable: 'GOOGLE_APPLICATION_CREDENTIALS'),
                        string(credentialsId: 'GITLAB_PERSONAL_ACCESS_TOKEN', variable: 'GITLAB_PERSONAL_ACCESS_TOKEN'),
                        string(credentialsId: 'JIRA_API_TOKEN', variable: 'JIRA_API_TOKEN'),
                        string(credentialsId: 'PROJECT_ID', variable: 'PROJECT_ID'),
                        string(credentialsId: 'LOCATION', variable: 'LOCATION'),
                        ]) {
                        sh '''
                        ./venv/bin/devai review code -c /bitnami/jenkins/home/workspace/genai-cicd_genai-for-developers/sample-app/src/main/java/anthos/samples/bankofanthos/balancereader
                        ./venv/bin/devai review performance -c /bitnami/jenkins/home/workspace/genai-cicd_genai-for-developers/sample-app/src/main/java/anthos/samples/bankofanthos/balancereader
                        ./venv/bin/devai review security -c /bitnami/jenkins/home/workspace/genai-cicd_genai-for-developers/sample-app/src/main/java/anthos/samples/bankofanthos/balancereader
                        '''
                    }
                }
            }
        }
    }
}
