# Balance Reader:  A Microservice for Bank Account Balances

## Description

This repository contains the code for the Balance Reader microservice, a Spring Boot application designed to track user account balances in a banking system. This microservice interacts with a shared ledger, receiving and processing real-time transaction updates to maintain accurate balances.

## Table of Contents

- [Description](#description)
- [Architecture](#architecture)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation and Deployment](#installation-and-deployment)
- [Configuration](#configuration)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Architecture

The Balance Reader service is designed to be a stateless microservice, relying on an in-memory cache for fast retrieval of account balances. The cache is periodically updated with new transactions received from the shared ledger.

**Key Components:**

- **Spring Boot Application:** Provides the framework for the service.
- **JWT Verifier:** Authenticates requests using JSON Web Tokens (JWTs) to ensure authorized access to account information.
- **Ledger Reader:** A background thread that continuously polls the shared ledger for new transaction updates.
- **Balance Cache:** A Guava cache for storing and retrieving account balances. 
- **Transaction Repository:** A Spring Data JPA repository for interacting with the database holding transaction information.
- **REST API:** Exposes endpoints for retrieving account balances and checking service health.

## Features

- **Real-Time Balance Updates:** The Balance Reader efficiently updates balances based on incoming transaction updates from the shared ledger.
- **Cache-Based Optimization:** Utilizes a local cache to improve the speed of balance retrieval.
- **Authorization:** Requires authentication with a valid JWT token for accessing user account balances.
- **Health Checks:** Provides readiness and liveness probes for monitoring service health.
- **Metrics Reporting:** Enables metrics reporting to Stackdriver for monitoring and analysis.

## Prerequisites

- **Java Development Kit (JDK):**  Version 11 or higher
- **Maven:**  A build tool for managing dependencies and building the project
- **Cloud SDK:**  The Google Cloud SDK for deploying the service to Google Cloud
- **kubectl:**  The Kubernetes command-line tool for interacting with Kubernetes clusters

## Installation and Deployment

1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd balance-reader
   ```

2. **Build the Project:**
   ```bash
   mvn clean install
   ```

3. **Configure Deployment Environment:**
   - Create a Kubernetes cluster on Google Cloud (e.g., using `gcloud container clusters create ...`).
   - Create a service account with the necessary permissions to access Cloud SQL and Stackdriver (see [Cloud IAM documentation](https://cloud.google.com/iam/docs)).
   - Download the service account key in JSON format.

4. **Configure Environment Variables:**
   - Set environment variables for configuration (e.g., `PUB_KEY_PATH`, `SPRING_DATASOURCE_URL`, etc.). You can use a `.env` file or export them in your terminal.

5. **Deploy to Kubernetes:**
   - Apply the Kubernetes configuration files located in the `deployment` directory:
     ```bash
     kubectl apply -f deployment/
     ```

## Configuration

The application is configured using environment variables and the `application.properties` file.

- **Key Configuration Properties:**
    - `server.port`: The port on which the service will listen.
    - `SPRING_DATASOURCE_URL`, `SPRING_DATASOURCE_USERNAME`, `SPRING_DATASOURCE_PASSWORD`: Database connection information.
    - `PUB_KEY_PATH`: The path to the public key used for JWT verification.
    - `LOCAL_ROUTING_NUM`: The bank routing number for the local branch.
    - `CACHE_SIZE`: The maximum size of the account balance cache.
    - `POLL_MS`: The interval (in milliseconds) for polling the transaction ledger for new transactions.
    - `ENABLE_TRACING`:  A flag to enable or disable tracing (set to `true` or `false`).
    - `ENABLE_METRICS`:  A flag to enable or disable metrics reporting (set to `true` or `false`).

## Usage

After deployment, you can access the Balance Reader REST API via the following endpoints:

- **`/version`:** Returns the service version.
- **`/ready`:** Checks if the service is ready to receive requests.
- **`/healthy`:** Checks if the service is healthy and serving requests.
- **`/balances/{accountId}`:** Retrieves the balance for the specified account.  Requires a valid JWT authentication token in the `Authorization` header.

## Testing

- **Unit Tests:**  The project includes unit tests for various components of the application.
- **Integration Tests:**  Use the `mvn test` command to run the integration tests, which verify the service's behavior in a realistic environment.

## Contributing

Contributions to the Balance Reader project are welcome!

1. **Fork the Repository:** Create a fork of the repository on GitHub.
2. **Create a Branch:** Create a new branch for your changes.
3. **Write Code and Tests:** Make your changes and write unit and integration tests to ensure the code's functionality.
4. **Submit a Pull Request:** Submit a pull request to the main repository, including a clear description of your changes.

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or issues, please open an issue on the repository's [GitHub issue tracker](https://github.com/google/cloud-samples/issues).
