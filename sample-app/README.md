# Balance Reader Service

This repository contains a Spring Boot application that provides a REST API for retrieving account balances from a ledger database. The service is designed to be deployed in a Kubernetes cluster and utilizes features like liveness and readiness probes, JWT authentication, and a cache for improved performance.

## Project Structure

The project follows a standard Spring Boot structure with the following key components:

- **src/main/java:** Contains the main source code, including the application entry point (`BalanceReaderApplication`), REST controller (`BalanceReaderController`), and business logic (`LedgerReader`, `BalanceCache`, `TransactionRepository`, etc.).
- **src/main/resources:** Holds configuration files like `application.properties`, `log4j2.xml`, and the banner (`banner.txt`).
- **src/test/java:** Contains JUnit tests for the service's functionality.
- **src/test/resources:** Contains test resources like mockito extensions.

## Features

- **REST API:** Exposes an endpoint `/balances/{accountId}` to retrieve the balance of a specific account.
- **JWT Authentication:** Authenticates requests using a JWT token provided in the Authorization header.
- **Ledger Integration:** Reads transaction data from a PostgreSQL database using Spring Data JPA.
- **Caching:** Caches account balances in memory for faster retrieval.
- **Liveness and Readiness Probes:** Provides endpoints for health checks, allowing Kubernetes to monitor the service's status.
- **Logging:** Utilizes Log4j2 for structured logging.
- **Metrics:** Exports metrics to Stackdriver for monitoring.

## Deployment

The application is intended to be deployed in a Kubernetes cluster. Deployment configurations are provided in the `deployment.yaml` file.

## Prerequisites

- **Java 11+**
- **Maven**
- **Kubernetes cluster**
- **Google Cloud Project** (for Stackdriver metrics)
- **PostgreSQL database**

## Installation and Configuration

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/balance-reader.git
   ```

2. **Set environment variables:**

   - `VERSION`: Service version.
   - `PORT`: Port number for the service.
   - `LOCAL_ROUTING_NUM`: Bank routing number for the local branch.
   - `PUB_KEY_PATH`: Path to the public key for JWT verification.
   - `SPRING_DATASOURCE_URL`: Connection URL for the PostgreSQL database.
   - `SPRING_DATASOURCE_USERNAME`: Username for the PostgreSQL database.
   - `SPRING_DATASOURCE_PASSWORD`: Password for the PostgreSQL database.

   You can set these variables in your Kubernetes deployment configuration or in the `application.properties` file.

3. **Build the application:**

   ```bash
   mvn clean package
   ```

4. **Deploy to Kubernetes:**

   ```bash
   kubectl apply -f deployment.yaml
   ```

## Usage

To retrieve the balance for an account, send a GET request to the `/balances/{accountId}` endpoint with a valid JWT token in the Authorization header:

```
curl -H "Authorization: Bearer <JWT_TOKEN>" http://<service-endpoint>/balances/<account_id>
```

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository.
2. Create a branch for your changes.
3. Make your changes and test them thoroughly.
4. Commit your changes and push to your branch.
5. Open a pull request to the main branch.

## License

This project is licensed under the Apache 2.0 License.

## Contact

For any questions or feedback, please contact [your email address].

## Documentation

- [Spring Boot Documentation](https://docs.spring.io/spring-boot/docs/current/reference/html/)
- [JWT Authentication](https://jwt.io/)
- [Stackdriver Monitoring](https://cloud.google.com/monitoring/)
- [PostgreSQL](https://www.postgresql.org/)
