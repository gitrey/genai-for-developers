## Balance Reader - Microservice for Bank Account Balances

This repository contains a Spring Boot microservice designed to track and retrieve bank account balances. The service consumes transactions from a ledger database and maintains a local cache of account balances.

**Features:**

* **Real-time Balance Updates:** The service listens for new transactions and updates the balance cache accordingly, providing real-time balance information.
* **Secure Authentication:** JWT-based authentication enforces access control, ensuring that only authorized users can retrieve account balances.
* **Robust Error Handling:** The service incorporates error handling for database connectivity issues and other potential failures.
* **Health and Readiness Checks:**  Liveness and readiness probes ensure the service is running healthily and can receive requests.
* **Metrics Monitoring:** The service exposes metrics for monitoring its performance and resource usage.

**Installation:**

1. Ensure you have Java 11+ and Maven installed.
2. Clone this repository.
3. Build the project using Maven: `mvn clean package`

**Deployment:**

This service is intended to be deployed as a containerized application. Follow these steps:

1. **Dockerfile:** Use the provided Dockerfile to build a container image.
2. **Kubernetes Deployment:**  Deploy the service using a Kubernetes deployment file.

**Configuration:**

The service uses environment variables to configure its behavior. You can customize the following:

* **`PORT`:** Port for the service to listen on.
* **`LOCAL_ROUTING_NUM`:** The bank routing number of the local bank branch.
* **`PUB_KEY_PATH`:** Path to the public key file for JWT verification.
* **`SPRING_DATASOURCE_URL`:** URL of the database containing transaction records.
* **`SPRING_DATASOURCE_USERNAME`:** Username for accessing the database.
* **`SPRING_DATASOURCE_PASSWORD`:** Password for accessing the database.
* **`ENABLE_TRACING`:** Enables or disables tracing using Spring Sleuth.
* **`ENABLE_METRICS`:** Enables or disables exporting metrics to Stackdriver.
* **`CACHE_SIZE`:** Maximum size of the account balance cache.
* **`POLL_MS`:** Time interval (in milliseconds) for polling the transaction ledger for new transactions.

**Dependencies:**

* **Spring Boot:** Web framework for building the service.
* **Spring Data JPA:** For interacting with the database.
* **Log4j2:** Logging framework.
* **JWT:** For JWT-based authentication.
* **Google Cloud Client Library for Java:** For accessing GCP services like Stackdriver Monitoring.
* **Guava:** For caching account balances.

**Code Structure:**

* **`src/main/java/anthos/samples/bankofanthos/balancereader`:** Contains the service logic.
    * **`BalanceReaderApplication.java`:** Main class.
    * **`BalanceReaderController.java`:** REST controller for handling API requests.
    * **`BalanceCache.java`:** Manages the account balance cache.
    * **`JWTVerifierGenerator.java`:** Generates a JWT verifier using the public key.
    * **`LedgerReader.java`:** Background thread responsible for polling the transaction ledger.
    * **`TransactionRepository.java`:** JPA repository interface for database interaction.
    * **`Transaction.java`:** Entity class representing a transaction.

**Example Usage:**

To retrieve the balance for account `12345` using a JWT token `your-jwt-token`, send a GET request to:

```
http://localhost:8080/balances/12345
```

with the `Authorization` header set to:

```
Authorization: Bearer your-jwt-token
```

**Contributing:**

Contributions to this project are welcome. Before contributing, please read the CONTRIBUTING.md file.

**License:**

This project is licensed under the Apache 2.0 License.
