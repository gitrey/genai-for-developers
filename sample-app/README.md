# BalanceReader: A Microservice for Account Balance Tracking

This repository contains the source code for the BalanceReader microservice. BalanceReader is a Spring Boot application designed to track the balance of bank accounts, ensuring efficient and reliable information for users. 

## Overview

The BalanceReader application acts as a backend component in a larger banking system. Its core functionalities include:

- **Account Balance Caching:** Maintains a local cache of account balances for quick retrieval.
- **Transaction Processing:** Continuously monitors a shared transaction ledger for new transactions.
- **Real-Time Balance Updates:** Dynamically updates account balances in the cache as new transactions occur.
- **REST API:** Exposes a REST endpoint to retrieve an account's current balance, secured with JWT authentication.
- **Health Checks:** Provides readiness and liveness probes to ensure service health and availability.
- **Metrics Monitoring:** Emits metrics for monitoring key aspects of the service (e.g., cache hits, request latency).

## Architecture

The BalanceReader application is built using the following technologies:

- **Spring Boot:** Provides a streamlined framework for building microservices.
- **Spring Data JPA:** Enables seamless interaction with the database.
- **Guava Cache:** Handles efficient caching of account balances.
- **JWT Authentication:** Secures access to sensitive data using JSON Web Tokens.
- **Log4j2:** Facilitates centralized logging for debugging and troubleshooting.
- **Stackdriver Monitoring:** Provides comprehensive metrics and logs for monitoring and observability.

## Getting Started

1. **Prerequisites:**

   - Java Development Kit (JDK) 11 or higher
   - Maven
   - Google Cloud SDK
   - A cloud SQL instance with a database schema setup for the `Transaction` entity.

2. **Configuration:**

   - **Environment Variables:** Configure the following environment variables:
      - `VERSION`: Service version string (e.g., "v1.0.0").
      - `PORT`: Port number for the service.
      - `LOCAL_ROUTING_NUM`: Routing number of the bank.
      - `PUB_KEY_PATH`: Path to the public key file for JWT authentication.
      - `SPRING_DATASOURCE_URL`: Database connection URL.
      - `SPRING_DATASOURCE_USERNAME`: Database username.
      - `SPRING_DATASOURCE_PASSWORD`: Database password.
      - `ENABLE_TRACING`: Enable or disable distributed tracing.
      - `ENABLE_METRICS`: Enable or disable metrics reporting.
      - `CACHE_SIZE`: Maximum size of the cache (default: 1,000,000).
      - `POLL_MS`: Interval for polling the transaction ledger (default: 100ms).

3. **Build and Run:**

   - From the root directory, run the following command to build the project:
     ```bash
     mvn clean package
     ```
   - Run the application using:
     ```bash
     mvn spring-boot:run 
     ```

## Usage

- Once the service is running, you can access the balance endpoint using a tool like curl.
- The `Authorization` header should include a valid JWT token for authentication.
- Replace `{accountId}` with the actual account number.
- The following command retrieves the balance for the specified account:

```bash
curl -H "Authorization: Bearer <jwt_token>" http://localhost:<port>/balances/{accountId}
```

## Monitoring

- **Stackdriver:** The BalanceReader service publishes metrics to Stackdriver, providing visibility into key performance indicators like:
    - Cache hit ratio
    - Transaction processing time
    - Request latency
    - Database connection health
- **Logs:** Log events are captured and stored in Stackdriver, facilitating debugging and troubleshooting.

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository and create a new branch for your changes.
2. Make your changes and write clear commit messages.
3. Run the tests and ensure they all pass.
4. Submit a pull request to the main branch for review.

## License

The BalanceReader microservice is licensed under the Apache 2.0 License.

## Contact

For any questions or issues, please open an issue on this repository.
