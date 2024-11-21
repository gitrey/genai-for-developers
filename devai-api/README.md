## Devai API

Devai API is a Python-based application built with the FastAPI framework. This API provides endpoints for generating code and documentation based on user prompts, as well as creating JIRA issues.

### Features

* **Code and Documentation Generation:** The `/generate` endpoint uses the Gemini 1.5 Pro model to generate code and documentation based on a user prompt.
* **JIRA Issue Creation:** The `/create-jira-issue` endpoint utilizes Gemini 1.5 Pro to create a detailed technical prompt for a JIRA user story based on provided requirements.
* **Test Endpoint:** The `/test` endpoint allows for testing the API functionality.

### Technologies Used

* **FastAPI:** Web framework for building APIs in Python.
* **Google Cloud AI Platform:** Cloud service for machine learning model development and deployment.
* **LangChain:** Library for building and deploying language models.
* **Vertex AI:** Cloud service for machine learning model development and deployment.
* **JIRA:** Project management tool.
* **GitLab:** Code hosting platform.

### Installation

1.  **Prerequisites:**
    * Python 3.11
    * Google Cloud SDK
    * Docker
    * A GCP project with Vertex AI and Cloud Run enabled
    * A JIRA account with API access
    * A GitLab account with API access
    * A LangSmith account with a service key
2.  **Set up the environment:**
    * Create a virtual environment:
        ```bash
        python3 -m venv venv-api
        . venv-api/bin/activate
        ```
    * Install dependencies:
        ```bash
        pip install -r requirements.txt
        ```
3.  **Configure environment variables:**
    * GCP Project ID:
        ```bash
        export PROJECT_ID=YOUR-GCP-PROJECT-ID
        ```
    * GCP Location:
        ```bash
        export LOCATION=us-central1
        ```
    * JIRA credentials:
        ```bash
        export JIRA_API_TOKEN=YOUR-JIRA-API-TOKEN
        export JIRA_USERNAME=YOUR-JIRA-USERNAME
        export JIRA_INSTANCE_URL=https://YOUR-JIRA-PROJECT.atlassian.net
        export JIRA_PROJECT_KEY=YOUR-JIRA-PROJECT-KEY
        export JIRA_CLOUD=true
        ```
    * GitLab credentials:
        ```bash
        export GITLAB_URL=https://gitlab.com
        export GITLAB_REPOSITORY=GITLAB-USERID/GITLAB-REPO
        export GITLAB_BRANCH=devai
        export GITLAB_BASE_BRANCH=main
        export GITLAB_PERSONAL_ACCESS_TOKEN=YOUR-GITLAB-PERSONAL-ACCESS-TOKEN
        ```
    * LangSmith credentials:
        ```bash
        export LANGCHAIN_TRACING_V2=true
        export LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
        export LANGCHAIN_API_KEY=YOUR-LANGCHAIN-API-KEY
        ```
4.  **Create secrets:**
    ```bash
    # JIRA API Token
    echo -n $JIRA_API_TOKEN | gcloud secrets create JIRA_API_TOKEN --data-file=-

    # GitLab Personal Access Token
    echo -n $GITLAB_PERSONAL_ACCESS_TOKEN | gcloud secrets create GITLAB_PERSONAL_ACCESS_TOKEN --data-file=-

    # LangChain API Key
    echo -n $LANGCHAIN_API_KEY | gcloud secrets create LANGCHAIN_API_KEY --data-file=-
    ```
5.  **Build the Docker image:**
    ```bash
    docker build -t devai-api .
    ```
6.  **Deploy the application to Cloud Run:**
    ```bash
    gcloud run deploy devai-api --source=. --region="$LOCATION" --allow-unauthenticated --service-account vertex-client --set-env-vars PROJECT_ID="$PROJECT_ID" --set-env-vars LOCATION="$LOCATION" --set-env-vars GITLAB_URL="$GITLAB_URL" --set-env-vars GITLAB_REPOSITORY="$GITLAB_REPOSITORY" --set-env-vars GITLAB_BRANCH="$GITLAB_BRANCH" --set-env-vars GITLAB_BASE_BRANCH="$GITLAB_BASE_BRANCH" --set-env-vars JIRA_USERNAME="$JIRA_USERNAME" --set-env-vars JIRA_INSTANCE_URL="$JIRA_INSTANCE_URL" --set-env-vars JIRA_PROJECT_KEY="$JIRA_PROJECT_KEY" --set-env-vars LANGCHAIN_TRACING_V2="$LANGCHAIN_TRACING_V2" --set-env-vars JIRA_CLOUD="$JIRA_CLOUD" --update-secrets="LANGCHAIN_API_KEY=LANGCHAIN_API_KEY:latest" --update-secrets="GITLAB_PERSONAL_ACCESS_TOKEN=GITLAB_PERSONAL_ACCESS_TOKEN:latest" --update-secrets="JIRA_API_TOKEN=JIRA_API_TOKEN:latest" --min-instances=1 --max-instances=3
    ```

### Usage

* **Generate Code and Documentation:**
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"prompt": "Create a Python function that takes two numbers as input and returns their sum."}' <your-cloud-run-service-url>/generate
    ```
* **Create a JIRA Issue:**
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"prompt": "Create a webpage to manage team off-site sessions. Session schema: id, time, topic, speaker. Provide HTML, JavaScript and CSS. Add backend API using FASTAPI framework."}' <your-cloud-run-service-url>/create-jira-issue
    ```

### Local Development

1.  **Clone the repository:**
    ```bash
    git clone <your-github-repo-url>
    ```
2.  **Navigate to the directory:**
    ```bash
    cd devai-api
    ```
3.  **Configure environment variables (refer to the Installation section).**
4.  **Start the application:**
    ```bash
    python run_app.py
    ```
5.  **Test the endpoints (refer to the Usage section).**

### Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and write clear, concise commit messages.
4.  Submit a pull request for review.

### License

Devai API is licensed under the Apache 2.0 License.

### Contact

For any questions or feedback, please contact us at <your-contact-email>.
