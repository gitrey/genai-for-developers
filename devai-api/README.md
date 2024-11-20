# Devai API

## Description

Devai API is a Python-based application built using the FastAPI framework. It serves as a backend for a GenAI agent, handling user requests and utilizing Google Gemini 1.5 Pro for code generation, documentation, and technical prompt creation for JIRA user stories. 

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Deployment](#deployment)
- [Local Development](#local-development)
- [Code Structure](#code-structure)
- [License](#license)
- [Contact](#contact)

## Features

- **Code Generation:**  Takes user prompts and generates code and documentation using the Gemini 1.5 Pro model.
- **JIRA Integration:**  Creates detailed technical JIRA user story prompts based on user input, enhancing the clarity of requirements.
- **GitLab Integration:**  Automates the creation of GitLab merge requests, including new files, commits, and pushing changes.
- **RESTful API:**  Provides a simple and accessible RESTful API for interacting with the GenAI agent.

## Deployment

### Prerequisites

- Google Cloud Platform Project
- Google Cloud SDK installed and authenticated
- Project ID and location (e.g., `us-central1`)

### Steps

1. **Set environment variables:**
   ```bash
   export PROJECT_ID=YOUR_GCP_PROJECT_ID
   export LOCATION=us-central1
   ```

2. **Authenticate with GCP:**
   ```bash
   gcloud auth login
   gcloud config set project $PROJECT_ID
   ```

3. **Create Secrets for API Tokens:**
   ```bash
   # JIRA API Token
   read -s JIRA_API_TOKEN
   export JIRA_API_TOKEN
   echo -n $JIRA_API_TOKEN | gcloud secrets create JIRA_API_TOKEN --data-file=-

   # GitLab Personal Access Token
   read -s GITLAB_PERSONAL_ACCESS_TOKEN
   export GITLAB_PERSONAL_ACCESS_TOKEN
   echo -n $GITLAB_PERSONAL_ACCESS_TOKEN | gcloud secrets create GITLAB_PERSONAL_ACCESS_TOKEN --data-file=-

   # LangChain API Key
   read -s LANGCHAIN_API_KEY
   export LANGCHAIN_API_KEY
   echo -n $LANGCHAIN_API_KEY | gcloud secrets create LANGCHAIN_API_KEY --data-file=- 
   ```

4. **Set other environment variables:**
   ```bash
   export JIRA_USERNAME="YOUR-EMAIL"
   export JIRA_INSTANCE_URL="https://YOUR-JIRA-PROJECT.atlassian.net"
   export JIRA_PROJECT_KEY="YOUR-JIRA-PROJECT-KEY"
   export JIRA_CLOUD=true

   export GITLAB_URL="https://gitlab.com"
   export GITLAB_REPOSITORY="GITLAB-USERID/GITLAB-REPO"
   export GITLAB_BRANCH="devai"
   export GITLAB_BASE_BRANCH="main"

   export LANGCHAIN_TRACING_V2=true
   export LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
   ```

5. **Deploy to Cloud Run:**
   ```bash
   gcloud run deploy devai-api \
     --source=. \
     --region="$LOCATION" \
     --allow-unauthenticated \
     --service-account vertex-client \
     --set-env-vars PROJECT_ID="$PROJECT_ID" \
     --set-env-vars LOCATION="$LOCATION" \
     --set-env-vars GITLAB_URL="$GITLAB_URL" \
     --set-env-vars GITLAB_REPOSITORY="$GITLAB_REPOSITORY" \
     --set-env-vars GITLAB_BRANCH="$GITLAB_BRANCH" \
     --set-env-vars GITLAB_BASE_BRANCH="$GITLAB_BASE_BRANCH" \
     --set-env-vars JIRA_USERNAME="$JIRA_USERNAME" \
     --set-env-vars JIRA_INSTANCE_URL="$JIRA_INSTANCE_URL" \
     --set-env-vars JIRA_PROJECT_KEY="$JIRA_PROJECT_KEY" \
     --set-env-vars LANGCHAIN_TRACING_V2="$LANGCHAIN_TRACING_V2" \
     --set-env-vars JIRA_CLOUD="$JIRA_CLOUD" \
     --update-secrets="LANGCHAIN_API_KEY=LANGCHAIN_API_KEY:latest" \
     --update-secrets="GITLAB_PERSONAL_ACCESS_TOKEN=GITLAB_PERSONAL_ACCESS_TOKEN:latest" \
     --update-secrets="JIRA_API_TOKEN=JIRA_API_TOKEN:latest" \
     --min-instances=1 \
     --max-instances=3
   ```

## Local Development

### Prerequisites

- Python 3.11
- Google Cloud SDK installed and authenticated
- Environment variables set as described in the [Deployment](#deployment) section
- LangSmith account (for tracing)

### Steps

1. **Navigate to the project directory:**
   ```bash
   cd ~/genai-for-developers/devai-api
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv-api
   . venv-api/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt 
   ```

4. **Start the application:**
   ```bash
   python run_app.py
   ```

5. **Test Endpoints:**
   - **JIRA Issue Creation:**
     ```bash
     curl -X POST -H "Content-Type: application/json" -d '{"prompt": "Create a webpage to manage team off-site sessions. Session schema: id, time, topic, speaker. Provide HTML, JavaScript and CSS. Add backend API using FASTAPI framework."}' http://localhost:8080/create-jira-issue
     ```
   - **GitLab Merge Request Creation:**
     ```bash
     curl -X POST -H "Content-Type: application/json" -d '{"prompt": "Create a webpage to manage team off-site sessions. Session schema: id, time, topic, speaker. Provide HTML, JavaScript and CSS. Add backend API using FASTAPI framework."}' http://localhost:8080/generate
     ```

## Code Structure

The code is structured into the following main components:

- **`devai-api/`:** Root directory.
  - **`app/`:** Contains the FastAPI application logic.
    - **`__init__.py`:** Entry point for the application.
    - **`app.py`:** FastAPI initialization and configuration.
    - **`constants.py`:** Defines global constants.
    - **`jira.py`:** Handles JIRA-related interactions.
    - **`routes.py`:** Defines API routes and handlers.
  - **`config.yml`:** Configuration file for the application.
  - **`Dockerfile`:**  Dockerfile for building a container image.
  - **`requirements.txt`:**  List of Python dependencies.
  - **`run_app.py`:**  Script to start the application.
  - **`local-dev.md`:** Instructions for local development.

## License

Devai API is licensed under the Apache 2.0 License. See the [LICENSE](./LICENSE) file for details.

## Contact

For any questions or issues, please open an issue on the GitHub repository: [link to GitHub repository]
