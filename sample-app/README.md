## README.md

# Bank of Anthos - Balance Reader

## Description

This repository contains the source code for the Balance Reader microservice, a component of the Bank of Anthos application. The Balance Reader is responsible for providing the current balance for a user's account. 

## Features

* **Authenticated Balance Retrieval:**  The service retrieves the balance for a specific account based on the provided JWT token, ensuring that the user is authorized to access the account.
* **Real-Time Balance Updates:** The service maintains a cached balance for each account and updates it in real-time based on incoming transactions.
* **Transaction Processing:** The Balance Reader listens for new transactions from the ledger and updates the balances of affected accounts.
* **Liveness and Readiness Probes:**  Includes endpoints for health checks, allowing for easy monitoring and automatic restart of the service in case of failures.
* **Metrics Reporting:** The Balance Reader publishes metrics to Stackdriver Monitoring, enabling observability and performance analysis.

## Table of Contents

- [Description](#description)
- [Architecture](#architecture)
- [Deployment](#deployment)
- [Running Locally](#running-locally)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Architecture

The Balance Reader microservice is built using the following technologies:

* **Spring Boot:**  Provides a foundation for building the REST API and managing application dependencies.
* **Spring Data JPA:**  Enables seamless interaction with a PostgreSQL database for storing and querying transactions.
* **Guava Cache:**  Implements an in-memory cache to improve performance and reduce latency for balance retrieval.
* **JWT Authentication:**  Utilizes JSON Web Tokens (JWT) for authentication, ensuring secure access to account balances.
* **Micrometer Stackdriver:**  Integrates with Google Cloud's Stackdriver monitoring to collect and report application metrics.
* **Logging with Log4j2:**  Provides comprehensive logging for debugging and troubleshooting.

## Deployment

The Balance Reader microservice can be deployed as a containerized application on Kubernetes. 

1. **Build the Docker Image:**
   ```bash
   mvn clean package jib:build
   ```

2. **Deploy to Kubernetes:**  
   Use your preferred Kubernetes deployment mechanism (e.g., kubectl, Helm). Ensure the deployment file includes the following configuration:

   * **Image:** Specify the built Docker image.
   * **Environment Variables:** Set the required environment variables for the service, including:
     * `VERSION`: The service version.
     * `PORT`: The port that the service will listen on.
     * `LOCAL_ROUTING_NUM`: The routing number of the bank branch.
     * `PUB_KEY_PATH`:  Path to the public key used for JWT verification.
     * `SPRING_DATASOURCE_URL`: The connection string to the PostgreSQL database.
     * `SPRING_DATASOURCE_USERNAME`: The username for the database.
     * `SPRING_DATASOURCE_PASSWORD`: The password for the database.

3. **Configure Stackdriver Monitoring:** Ensure that your Kubernetes cluster is configured to send metrics to Stackdriver Monitoring. Refer to the Stackdriver documentation for instructions.

## Running Locally

You can run the Balance Reader locally for development and testing.

1. **Set up Environment Variables:**  Create a `.env` file in the project root directory and define the required environment variables as described in the [Deployment](#deployment) section.

2. **Run the Application:**  Execute the following command:
   ```bash
   mvn spring-boot:run
   ```

3. **Access the API:**  The Balance Reader API will be accessible at `http://localhost:8080`. For example, to retrieve the balance for an account, use the following URL (replace `your_account_id` with the actual account ID):

   ```bash
   http://localhost:8080/balances/your_account_id
   ```
   
   Ensure to include a valid JWT token in the `Authorization` header of your request (e.g., `Bearer <your_jwt_token>`).

## Testing

The Balance Reader includes unit tests to ensure code quality and functional correctness.

1. **Run Unit Tests:**
   ```bash
   mvn test
   ```

## Contributing

We welcome contributions from the community! To contribute to the Balance Reader:

1. **Fork the Repository:** Create a fork of the project on GitHub.
2. **Create a Branch:** Create a new branch for your feature or bug fix.
3. **Make Changes:** Implement your changes and write comprehensive tests.
4. **Submit a Pull Request:** Submit a pull request to the main repository, detailing your changes and providing relevant context.

## License

The Balance Reader is licensed under the Apache 2.0 License.

## Contact

For any questions or feedback, please open an issue on the project's GitHub repository: [Link to GitHub repository]
