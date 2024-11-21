# Balance Reader Microservice

This repository contains the code for a simple microservice that reads and caches account balances from a shared ledger. The service uses a JWT authentication scheme for authorization and integrates with Google Cloud's Stackdriver for monitoring and logging. 

## Table of Contents

- [Project Description](#project-description)
- [Prerequisites](#prerequisites)
- [Setup & Deployment](#setup-and-deployment)
- [Code Overview](#code-overview)
- [Microservice Architecture](#microservice-architecture)
- [Security Considerations](#security-considerations)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Project Description

This microservice is part of a larger banking application system. It is responsible for:

- Retrieving the current balance of an account from a shared ledger.
- Caching the balance in memory to improve performance.
- Authenticating users using JWT tokens.
- Providing health and readiness probes for monitoring.
- Exporting metrics to Stackdriver for monitoring.

## Prerequisites

- Java Development Kit (JDK) 11 or later.
- Maven or Gradle build tool.
- A Google Cloud Platform project with the following enabled:
    - Cloud SQL
    - Stackdriver Logging
    - Stackdriver Monitoring

## Setup & Deployment

**1. Clone the repository:**

```bash
git clone https://github.com/google/cloud-samples/
```

**2. Configure the project:**

- **Replace placeholders:** Update the values in the `application.properties` file with your specific configuration:
    - `PORT`: Port for the microservice to listen on.
    - `LOCAL_ROUTING_NUM`: Routing number of the local bank.
    - `PUB_KEY_PATH`: Path to the public key for JWT verification.
    - `SPRING_DATASOURCE_URL`: URL of the Cloud SQL instance.
    - `SPRING_DATASOURCE_USERNAME`: Username for the Cloud SQL instance.
    - `SPRING_DATASOURCE_PASSWORD`: Password for the Cloud SQL instance.
    - `CACHE_SIZE`: Maximum size of the in-memory cache.
    - `POLL_MS`: Interval (in milliseconds) for polling the ledger for new transactions.
    - `ENABLE_TRACING`: Enable or disable tracing (set to `true` or `false`).
    - `ENABLE_METRICS`: Enable or disable metric exporting (set to `true` or `false`).
- **Setup Cloud SQL:** Create a Cloud SQL instance and set up a database for storing the transactions.
- **Create a service account:** Create a service account with the necessary permissions to access Cloud SQL.
- **Download the public key:** Create a public key and download it to the specified path in `PUB_KEY_PATH`.
- **Set environment variables:** Set the environment variables specified in the `application.properties` file.

**3. Build the project:**

- **Maven:** Run `mvn clean package` in the project directory.
- **Gradle:** Run `./gradlew build` in the project directory.

**4. Deploy the project:**

- **Deploy using Kubernetes:** 
    - Deploy the microservice to a Kubernetes cluster.
    - Configure a Kubernetes Ingress to expose the microservice on a public endpoint.
    - Create a service account and grant it access to Cloud SQL.
- **Deploy using Google Cloud Run:** 
    - Deploy the microservice to Google Cloud Run.
    - Configure Cloud Run to use the service account for access to Cloud SQL.
    - Enable Stackdriver monitoring for the service.

## Code Overview

The code is organized into several key components:

- **BalanceReaderApplication:** The main application class, responsible for initializing the Spring Boot application.
- **BalanceReaderController:** REST controller handling requests to the `/balances/{accountId}` endpoint.
- **JWTVerifierGenerator:** Generates a JWT verifier using a public key.
- **BalanceCache:** Manages the in-memory cache for account balances.
- **TransactionRepository:** Interface for accessing the transaction database.
- **LedgerReader:** Background thread that listens for new transactions in the ledger and updates the cache.
- **Transaction:** Represents a transaction in the ledger.

## Microservice Architecture

The microservice utilizes the following design patterns:

- **Event-driven architecture:** The LedgerReader listens for new transactions in the ledger, triggering updates to the cache.
- **Caching:** The in-memory cache improves performance by reducing database queries.
- **REST API:** Provides a simple API for accessing account balances.
- **Layered architecture:** The code is separated into distinct layers for presentation, business logic, and data access.

## Security Considerations

- **JWT authentication:** The microservice uses JWT tokens for authentication and authorization, ensuring that only authorized users can access account balances.
- **Public key security:** The public key used for JWT verification is stored securely in the application configuration.
- **Database security:** The Cloud SQL instance is configured with appropriate security settings to protect sensitive data.

## Testing

- Unit tests are included for key components of the code.
- Integration tests can be implemented to test the end-to-end functionality of the microservice.
- The microservice should be thoroughly tested in a staging environment before deploying to production.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and write tests.
4. Submit a pull request for review.

## License

The code in this repository is licensed under the Apache 2.0 License.
