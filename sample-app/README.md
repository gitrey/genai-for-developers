## Balance Reader Microservice

This repository contains a Spring Boot microservice that reads transaction data from a database and maintains a cached balance for user accounts. The service is designed to be deployed in a Kubernetes cluster and uses various tools and technologies for monitoring, tracing, and authentication.

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Dependencies](#dependencies)
- [Setup and Configuration](#setup-and-configuration)
- [Running the Service](#running-the-service)
- [Testing](#testing)
- [Monitoring and Logging](#monitoring-and-logging)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Balance Reader microservice acts as a backend service for a banking application. It retrieves balance information for users based on their account IDs. The service uses a database to store transaction records and a cache to improve performance for retrieving balances. 

## Architecture

The service follows a typical microservice architecture:

1. **REST API:** Exposes an endpoint (`/balances/{accountId}`) to fetch account balances.
2. **Authentication:** JWT authentication is used to verify user access to specific accounts.
3. **Database:** Transactions are stored in a relational database using JPA.
4. **Cache:** Guava Cache is used to store recently accessed account balances.
5. **Ledger Reader:** A background thread continuously polls the database for new transactions and updates the cache.

## Dependencies

- **Spring Boot:** Framework for building the microservice.
- **Spring Data JPA:** Abstraction for interacting with the database.
- **Guava Cache:** Library for implementing the cache.
- **Log4j2:** Logging framework.
- **JWT:** Library for JWT authentication.
- **Micrometer:** Metrics library for monitoring.
- **Stackdriver:** Integration with Google Cloud Stackdriver for monitoring.

## Setup and Configuration

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/balance-reader.git
   cd balance-reader
   ```

2. **Environment Variables:**
   - Set the following environment variables:
     - `VERSION`: The version of the service.
     - `PORT`: The port for the service to listen on.
     - `LOCAL_ROUTING_NUM`: The routing number of the bank this service is responsible for.
     - `PUB_KEY_PATH`: The path to the public key file used for JWT verification.
     - `SPRING_DATASOURCE_URL`: The URL of the database.
     - `SPRING_DATASOURCE_USERNAME`: The database username.
     - `SPRING_DATASOURCE_PASSWORD`: The database password.
     - `ENABLE_TRACING`: Set to `true` or `false` to enable or disable tracing (optional).
     - `ENABLE_METRICS`: Set to `true` or `false` to enable or disable metrics export (optional).

3. **Database Setup:**
   - Ensure the database is accessible with the provided credentials and that the database schema is created (using the `Transaction` entity).

## Running the Service

1. **Build the Application:**
   ```bash
   mvn clean package
   ```

2. **Run the Service:**
   ```bash
   java -jar target/balance-reader-*.jar
   ```

## Testing

The project includes unit tests to verify the functionality of the service. You can run the tests using the following command:

```bash
mvn test
```

## Monitoring and Logging

- **Logging:** Log4j2 is configured to write logs to the console with timestamps and severity levels.
- **Metrics:** Micrometer is integrated to collect and export metrics to Stackdriver.
- **Tracing:** OpenTelemetry tracing can be enabled for tracking requests across services.

## Contributing

We welcome contributions! To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and ensure they pass all tests.
4. Submit a pull request for review.

## License

This project is licensed under the Apache 2.0 License.
