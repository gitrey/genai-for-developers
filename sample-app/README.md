# BalanceReader - A Bank of Anthos Microservice

## Overview

This repository contains the source code for `BalanceReader`, a simple microservice that demonstrates the use of gRPC for communication and a database for data storage within a Bank of Anthos application. It provides a REST API for retrieving the current balance of a user's account based on JWT authentication.

## Project Structure

The project is organized as follows:

- **src/main/java:** Contains the Java source code for the application.
    - **anthos.samples.bankofanthos.balancereader:** Contains the main application logic, including:
        - **BalanceReaderApplication:** Main entry point for the application.
        - **BalanceReaderController:** REST controller for handling requests.
        - **BalanceCache:** Class responsible for caching account balances.
        - **JWTVerifierGenerator:** Class responsible for generating a JWT verifier.
        - **LedgerReader:** Background thread that monitors for new transactions.
        - **TransactionRepository:** Interface for accessing the Transaction database.
        - **Transaction:** Entity class representing a transaction.
- **src/main/resources:** Contains configuration files.
    - **log4j2.xml:** Configuration for the Log4j2 logging framework.
    - **banner.txt:** Text banner displayed on application startup.
    - **application.properties:** Configuration for the Spring Boot application.

## Dependencies

The project utilizes the following dependencies:

- **Spring Boot:** Framework for building the application.
- **Spring Data JPA:** Library for interacting with the database.
- **gRPC:** Library for communication with the Ledger microservice.
- **Auth0 Java JWT:** Library for verifying JWT tokens.
- **Google Cloud Metadata:** Library for retrieving metadata about the running environment.
- **Micrometer Stackdriver:** Library for exporting metrics to Stackdriver Monitoring.

## Usage

To run the application:

1. **Set environment variables:** Set the following environment variables:

   - `VERSION`: The version of the application.
   - `PORT`: The port number for the application to listen on.
   - `LOCAL_ROUTING_NUM`: The routing number of the bank.
   - `PUB_KEY_PATH`: The path to the public key file used for JWT verification.
   - `SPRING_DATASOURCE_URL`: The connection URL for the database.
   - `SPRING_DATASOURCE_USERNAME`: The username for the database.
   - `SPRING_DATASOURCE_PASSWORD`: The password for the database.
   - `ENABLE_TRACING`: Whether to enable tracing with Sleuth.
   - `ENABLE_METRICS`: Whether to enable exporting metrics to Stackdriver Monitoring.
   - `CACHE_SIZE`: The maximum size of the account balance cache.
   - `POLL_MS`: The interval (in milliseconds) for polling the Ledger for new transactions.

2. **Build the application:** Execute the following command:

   ```bash
   mvn clean package
   ```

3. **Run the application:** Execute the following command:

   ```bash
   java -jar target/balance-reader-*.jar
   ```

## API Endpoints

The application exposes the following REST API endpoints:

- `/version`: Returns the version of the application.
- `/ready`: Readiness probe endpoint.
- `/healthy`: Liveness probe endpoint.
- `/balances/{accountId}`: Returns the current balance for the specified account. Requires a valid JWT token in the `Authorization` header.

## Authentication

The application uses JWT authentication to verify the identity of the user making a request. The JWT token is expected to have the following claim:

- `acct`: The account ID of the user.

The JWT token is verified against the public key specified in the `PUB_KEY_PATH` environment variable.

## Database

The application stores account balances in a database. The database connection information is provided through the following environment variables:

- `SPRING_DATASOURCE_URL`
- `SPRING_DATASOURCE_USERNAME`
- `SPRING_DATASOURCE_PASSWORD`

## Tracing

The application supports tracing with Sleuth. Tracing can be enabled by setting the `ENABLE_TRACING` environment variable to `true`.

## Metrics

The application exports metrics to Stackdriver Monitoring. Metrics can be enabled by setting the `ENABLE_METRICS` environment variable to `true`.

## Contributing

Contributions are welcome! Please submit pull requests to the repository.

## License

This project is licensed under the Apache 2.0 License.

## Contact

For any questions or feedback, please contact the project maintainers.
