# BalanceReader: A Microservice for Tracking Bank Account Balances

This repository contains the code for a microservice called BalanceReader. This service tracks the current balance for each user account in a distributed banking system. It utilizes a shared transaction ledger and a local cache to provide fast and efficient balance retrieval.

## Project Structure

The project is organized as follows:

* **src/main/java/anthos/samples/bankofanthos/balancereader/**: Contains the Java source code for the BalanceReader microservice. 
    * **BalanceCache.java**: Manages the local cache for account balances.
    * **BalanceReaderApplication.java**: The main application entry point.
    * **BalanceReaderController.java**: Handles REST API requests for balance retrieval.
    * **JWTVerifierGenerator.java**: Generates a JWT verifier for authentication.
    * **LedgerReader.java**: Monitors the shared transaction ledger for new transactions and updates the local cache.
    * **Transaction.java**: Represents a banking transaction.
    * **TransactionRepository.java**: Provides access to the transaction database. 

* **src/main/resources/**: Contains configuration files for the BalanceReader service.
    * **log4j2.xml**: Configuration file for the logging framework.
    * **application.properties**: Application configuration properties, including database connection information and tracing settings.
    * **banner.txt**: Custom banner displayed when the application starts.

## Dependencies

The BalanceReader microservice relies on the following libraries:

* **Spring Boot**: Provides a framework for building microservices.
* **Spring Data JPA**: Enables easy access to a relational database.
* **Guava Cache**: Provides a fast and efficient local cache.
* **Auth0 JWT**: Used for JWT authentication.
* **Google Cloud Metadata**: Used for retrieving the project ID and other metadata from Google Cloud.
* **Micrometer**: Enables metrics collection and reporting.
* **Stackdriver**: Provides a backend for storing and analyzing metrics.
* **Log4j**: Provides logging functionality.

## Requirements

* **Java 8 or higher**: To run the BalanceReader microservice.
* **Maven or Gradle**: To build the project.
* **Google Cloud Platform (GCP) account**: For deploying and running the microservice.
* **A relational database**: To store the transactions.

## Installation and Setup

1. **Set up a GCP Project**:
   * Create a new GCP project or use an existing one.
   * Enable the Cloud SQL API for your project.
   * Create a new Cloud SQL instance with a database for storing transactions.

2. **Clone the repository**: 
   * Run the following command to clone the repository:
     ```bash
     git clone https://github.com/GoogleCloudPlatform/microservices-demo.git
     cd microservices-demo/sample-app
     ```

3. **Set environment variables**:
   * Set the following environment variables:
     * `VERSION`: The version of your service.
     * `PORT`: The port on which the service should listen (e.g., 8080).
     * `LOCAL_ROUTING_NUM`: The routing number for the local bank.
     * `PUB_KEY_PATH`: Path to the public key used for JWT verification.
     * `SPRING_DATASOURCE_URL`: The JDBC URL for connecting to your Cloud SQL database.
     * `SPRING_DATASOURCE_USERNAME`: The username for connecting to your Cloud SQL database.
     * `SPRING_DATASOURCE_PASSWORD`: The password for connecting to your Cloud SQL database.

4. **Build the project**:
   * Use Maven or Gradle to build the project.
   * The built JAR file will be located in the `target` directory.

5. **Deploy to GCP**: 
   * Use Google Cloud tools (e.g., `gcloud`, `kubectl`) to deploy the microservice to your GCP project.
   * Follow the instructions in the [Deployment](docs/deployment.md) guide for specific steps.

## Usage

The BalanceReader microservice provides a single REST endpoint for retrieving account balances:

* **GET /balances/{accountId}**: Retrieves the balance for the specified account ID.

The endpoint requires authentication using a JWT token in the `Authorization` header. The JWT token should contain the account ID in the `acct` claim.

## Tracing

The BalanceReader microservice includes tracing capabilities, which can be enabled by setting the `ENABLE_TRACING` environment variable to `true`. When tracing is enabled, the microservice will generate traces that can be analyzed in a tracing system such as OpenTelemetry or Jaeger.

## Metrics

The BalanceReader microservice also collects and exports metrics using Micrometer and Stackdriver. 

## Logging

The BalanceReader microservice uses Log4j for logging. The log level can be configured using the `LOG_LEVEL` environment variable. The default log level is `INFO`.

## Contributing

Contributions are welcome! Please refer to the [Contributing](CONTRIBUTING.md) guide for more information.

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.
