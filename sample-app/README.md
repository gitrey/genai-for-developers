## Bank of Anthos - Balance Reader

This repository contains the source code for the Bank of Anthos Balance Reader microservice. This service is responsible for providing a REST API to retrieve the current balance for authenticated users.

## Table of Contents

- [Description](#description)
- [Architecture](#architecture)
- [Setup & Deployment](#setup--deployment)
- [Usage](#usage)
- [Testing](#testing)
- [Monitoring](#monitoring)
- [Contributing](#contributing)
- [License](#license)

## Description

The Balance Reader microservice is a key component of the Bank of Anthos application. It acts as a bridge between the user interface and the bank ledger database, ensuring secure and efficient access to account balances.

## Architecture

The service follows a microservice architecture and is built with Spring Boot, providing a REST API. The key components include:

* **BalanceReaderController:** Handles REST requests, authenticates users using JWT, and retrieves balances from the cache.
* **LedgerReader:** Continuously polls the database for new transactions, applying them to the cache and notifying the BalanceReaderController about updates.
* **TransactionRepository:** Provides access to the underlying database, handling queries for balances and transactions.
* **BalanceCache:** A Guava LoadingCache that stores account balances, optimizing read operations.
* **JWTVerifierGenerator:** Generates a JWT verifier for authenticating user requests.

## Setup & Deployment

1. **Prerequisites:**
   - Java Development Kit (JDK) 11
   - Maven 3.6.x or higher
   - Google Cloud SDK installed and authenticated
   - Docker

2. **Setup:**
   - Clone this repository: `git clone <repository_url>`
   - Set environment variables:
     ```bash
     export VERSION=<service_version>
     export PORT=<port_number>
     export LOCAL_ROUTING_NUM=<local_routing_number>
     export PUB_KEY_PATH=<path_to_public_key>
     export SPRING_DATASOURCE_URL=<database_url>
     export SPRING_DATASOURCE_USERNAME=<database_username>
     export SPRING_DATASOURCE_PASSWORD=<database_password>
     ```
   - Build the application: `mvn clean package`

3. **Deployment:**
   - Create a Dockerfile:
     ```dockerfile
     FROM openjdk:11-jre-slim
     COPY target/bank-of-anthos-balance-reader-*.jar /app.jar
     ENTRYPOINT ["java", "-jar", "/app.jar"]
     ```
   - Build the Docker image: `docker build -t bank-of-anthos-balance-reader .`
   - Deploy the image to your preferred container orchestration platform (e.g., Kubernetes, Cloud Run)

## Usage

The Balance Reader service provides the following REST endpoints:

* **GET /version:** Returns the service version.
* **GET /ready:** Health check endpoint, returns "ok" if the server is ready to receive requests.
* **GET /healthy:** Liveness probe endpoint, returns "ok" if the server is healthy and serving requests.
* **GET /balances/{accountId}:** Returns the balance for the specified account. Requires a valid JWT token in the Authorization header.

## Testing

The project includes JUnit tests for the BalanceReaderController and other components. To run the tests:

```bash
mvn test
```

## Monitoring

The Balance Reader service utilizes Micrometer for monitoring metrics. Metrics are automatically exported to Stackdriver if enabled.

**Configuration:**

- **ENABLE_METRICS:** Environment variable to toggle metrics export (default: true)

## Contributing

Contributions to this project are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes, adhering to the project's style guide.
4. Write tests for your changes.
5. Submit a pull request, clearly describing your changes.

## License

This project is licensed under the Apache 2.0 License.

##  Next Steps

- Explore the other components of the Bank of Anthos application.
- Extend the Balance Reader service with more features, such as transaction history retrieval.
- Enhance the monitoring capabilities by adding custom metrics.
