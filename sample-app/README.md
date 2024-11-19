## BalanceReader: A Microservice for Real-time Account Balance Tracking

This repository contains a microservice called "BalanceReader," designed to efficiently track and provide real-time account balance information for users. The service leverages a combination of caching, background processing, and database interaction to achieve high performance and responsiveness.

## Project Structure

The project is structured as follows:

* **`src/main/java/anthos/samples/bankofanthos/balancereader`**: Contains the core Java code for the microservice, including:
    * **`BalanceReaderApplication.java`**: The Spring Boot entry point for the application.
    * **`JWTVerifierGenerator.java`**: Generates a JWT verifier for authentication purposes.
    * **`BalanceCache.java`**: Manages the account balance cache using Guava's `LoadingCache`.
    * **`BalanceReaderController.java`**: Exposes the REST API endpoints for retrieving account balances.
    * **`LedgerReader.java`**: Continuously monitors the transaction ledger for updates and processes transactions to update the balance cache.
    * **`TransactionRepository.java`**: Spring Data JPA repository interface for accessing the transaction database.
    * **`Transaction.java`**: Represents a banking transaction entity.

* **`src/main/resources`**: Contains configuration files:
    * **`log4j2.xml`**: Log4j2 configuration file for logging.
    * **`banner.txt`**: Custom banner for the application.
    * **`application.properties`**: Spring Boot configuration file.

## Requirements

* **Java 11+**
* **Maven**
* **Spring Boot**
* **Google Cloud SDK**
* **MySQL** or **PostgreSQL** database

## Installation and Setup

1. **Set up a database:** Create a database instance (MySQL or PostgreSQL) and configure the following environment variables:
    * `SPRING_DATASOURCE_URL`: URL of the database instance.
    * `SPRING_DATASOURCE_USERNAME`: Username for the database instance.
    * `SPRING_DATASOURCE_PASSWORD`: Password for the database instance.
2. **Clone the repository:**
    ```bash
    git clone https://github.com/GoogleCloudPlatform/microservices-demo.git
    cd microservices-demo/sample-app
    ```
3. **Install dependencies:**
    ```bash
    mvn clean install
    ```
4. **Set environment variables:**
    * `VERSION`: The version of the service (e.g., "v1.0.0").
    * `PORT`: The port on which the service will run (e.g., "8080").
    * `LOCAL_ROUTING_NUM`: The routing number of the bank branch served by this instance.
    * `PUB_KEY_PATH`: The path to the public key file used for JWT verification.
    * `CACHE_SIZE`: The maximum size of the balance cache (default: 1000000).
    * `POLL_MS`: The frequency (in milliseconds) at which the `LedgerReader` polls the transaction ledger for updates (default: 100).
    * `ENABLE_TRACING`: Toggle tracing on/off (default: false).
    * `ENABLE_METRICS`: Toggle metrics export on/off (default: true). 
    * `LOG_LEVEL`: The logging level (default: INFO).
5. **Run the application:**
    ```bash
    mvn spring-boot:run
    ```

## Usage

Once the application is running, you can access the following REST API endpoints:

* **`/version`**: Returns the service version.
* **`/ready`**: Readiness probe endpoint. Returns "ok" if the server is ready to receive requests.
* **`/healthy`**: Liveness probe endpoint. Returns "ok" if the server is healthy and serving requests.
* **`/balances/{accountId}`**: Returns the balance for the specified account. Requires a valid JWT token in the `Authorization` header.

## JWT Authentication

The service uses JWT authentication to ensure secure access to account balance information. The JWT token must contain an `acct` claim that specifies the account ID.

## Tracing and Metrics

The application supports tracing and metrics for observability.

* **Tracing**: When `ENABLE_TRACING` is set to `true`, tracing is enabled using Spring Cloud Sleuth, sending traces to Zipkin. 
* **Metrics**: Metrics are exported to Stackdriver using Micrometer. The `ENABLE_METRICS` environment variable controls metrics export.

## Contributing

Contributions are welcome! Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.
