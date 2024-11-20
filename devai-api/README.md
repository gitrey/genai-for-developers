# Devai API

## Description

Devai API is a Python-based application built with the FastAPI framework. It provides a set of endpoints designed to interact with large language models and automate tasks related to code generation, documentation, and project management.

This API serves as the backend for a GenAI agent, allowing users to interact with the API via a simple interface for various tasks.

## Features

- **Code & Documentation Generation:**  The `/generate` endpoint takes a user prompt and utilizes the Gemini 1.5 Pro model to generate code and accompanying documentation based on the provided requirements.
- **JIRA Issue Creation:** The `/create-jira-issue` endpoint accepts a user prompt and leverages the Gemini 1.5 Pro model to create a detailed technical prompt for a JIRA user story based on the input.
- **GitLab Integration:** The `/generate` endpoint can be integrated with GitLab to automatically create merge requests with the generated code and documentation.
- **Testing Endpoint:**  The `/test` endpoint allows for testing of the API's functionality.

## Installation

To install Devai API:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/devai-api.git
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd devai-api
    ```

3.  **Create a virtual environment:**
    ```bash
    python3 -m venv venv-api
    source venv-api/bin/activate
    ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running Locally

**Prerequisites:**

- **Google Cloud Account:** Create a Google Cloud project and enable the required services (Vertex AI, Secret Manager).
- **JIRA Account:** Obtain a JIRA account with API access.
- **GitLab Account:** Obtain a GitLab account with API access.
- **LangSmith Account:** Obtain a LangSmith account and API key.

**Setup:**

1.  **Set Environment Variables:** Follow the instructions in the `local-dev.md` file to set up the required environment variables for your Google Cloud project, JIRA, GitLab, and LangSmith.
2.  **Start the Application:**
    ```bash
    python run_app.py
    ```

## Deployment

### Cloud Run

1.  **Set up GCP Project:** Follow the instructions in the `README.md` file to set up your GCP project, enable the required services, and authenticate.
2.  **Set Secrets:** Create secrets in Secret Manager for `JIRA_API_TOKEN`, `GITLAB_PERSONAL_ACCESS_TOKEN`, and `LANGCHAIN_API_KEY` as outlined in the `README.md` file.
3.  **Deploy to Cloud Run:** Run the deployment command provided in the `README.md` file.

## Usage

**API Endpoints:**

- **`/`:** Root endpoint, returns a welcome message.
- **`/test`:** Test endpoint, sends a query to the Gemini 1.5 model and returns the response.
- **`/generate`:** Endpoint for code and documentation generation. Accepts a user prompt in the request body and returns the generated content.
- **`/create-jira-issue`:** Endpoint for JIRA issue creation. Accepts a user prompt in the request body and creates a new JIRA issue with a detailed technical description.

**Example Usage:**

```bash
# Generate code and documentation
curl -X POST -H "Content-Type: application/json" -d '{"prompt": "Create a simple Python program to calculate the factorial of a number."}' http://localhost:8080/generate

# Create a JIRA issue
curl -X POST -H "Content-Type: application/json" -d '{"prompt": "Create a webpage to manage team off-site sessions. Session schema: id, time, topic, speaker. Provide HTML, JavaScript and CSS. Add backend API using FASTAPI framework."}' http://localhost:8080/create-jira-issue
```

## Contributing

Contributions are welcome! Please follow our style guide and submit pull requests. Refer to the `CONTRIBUTING.md` file for more details.

## License

Devai API is released under the Apache 2.0 License. See the `LICENSE` file for more information.

## Contact

For any questions or feedback, please contact us at:

- **GitHub Repository:** [Link to GitHub repository]
- **Email:** [Your email address]
