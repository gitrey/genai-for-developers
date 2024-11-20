# BalanceReader Service

This repository contains a sample Spring Boot microservice that reads balance updates from a shared ledger and serves them to clients. It demonstrates the following features:

* **Microservice Architecture:** The service is designed as a self-contained unit, interacting with other services through APIs.
* **Database Integration:** It utilizes Spring Data JPA for interacting with a transactional database.
* **Authentication:** The service enforces authentication using JWT tokens.
* **Caching:** It utilizes Guava Cache for improving performance by storing frequently accessed data in memory.
* **Monitoring:** It implements metrics for monitoring performance and resource usage.
* **Liveness and Readiness Probes:**  It includes health check endpoints for container orchestration.

## Architecture

The service consists of the following components:

* **BalanceReaderController:** Handles incoming requests from clients for account balances.
* **LedgerReader:** Continuously monitors a shared ledger for new transaction updates.
* **TransactionRepository:** Interface for accessing and querying transactions stored in the database.
* **Transaction:** Entity class representing a single transaction.
* **BalanceCache:** Manages caching of account balances for faster retrieval.
* **JWTVerifierGenerator:** Generates a JWT verifier for token authentication.

## Installation and Running

**Prerequisites:**

* Java Development Kit (JDK) 11+
* Maven or Gradle
* Docker (optional, for running with Docker)

**Steps:**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/GoogleCloudPlatform/microservices-demo.git
   cd microservices-demo/sample-app
   ```

2. **Build the application:**
   ```bash
   mvn clean package
   ```

3. **Run the application:**
   ```bash
   mvn spring-boot:run
   ```
   Or, run using Docker:
   ```bash
   docker build -t balance-reader .
   docker run -p 8080:8080 -e ENABLE_METRICS=true -e ENABLE_TRACING=true -e PUB_KEY_PATH=/app/src/main/resources/public.pem balance-reader 
   ```

## Configuration

The service can be configured using environment variables or a `application.properties` file:

* **PORT:** Port number for the service (default: 8080)
* **LOCAL_ROUTING_NUM:** The local routing number for the bank.
* **PUB_KEY_PATH:** Path to the public key for JWT verification.
* **SPRING_DATASOURCE_URL:** Database connection URL.
* **SPRING_DATASOURCE_USERNAME:** Database username.
* **SPRING_DATASOURCE_PASSWORD:** Database password.
* **CACHE_SIZE:** Maximum size of the cache (default: 1000000).
* **POLL_MS:** Interval in milliseconds for checking new transactions (default: 100).
* **ENABLE_METRICS:** Enable/disable metrics collection (default: true).
* **ENABLE_TRACING:** Enable/disable tracing (default: true).

## Usage

The BalanceReader service exposes the following endpoints:

* **`/version`:** Returns the service version.
* **`/ready`:** Readiness probe endpoint.
* **`/healthy`:** Liveness probe endpoint.
* **`/balances/{accountId}`:** Retrieves the balance for the specified account.

To use the `/balances/{accountId}` endpoint, you need to provide a valid JWT token in the `Authorization` header. The token should contain the user's account ID in the `acct` claim.

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your changes.
3. Commit your changes with clear and concise commit messages.
4. Push your changes to your forked repository.
5. Submit a pull request for review.

## License

This code is licensed under the Apache 2.0 License.

## Contact

If you have any questions or feedback, please open an issue on this repository.
