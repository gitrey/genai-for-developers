## BalanceReader - A Microservice for Account Balance Tracking

This repository contains the source code for the BalanceReader microservice, a simple application that demonstrates how to interact with a shared database and track balances based on transactions from a transaction ledger.

**Table of Contents**

- [Description](#description)
- [Features](#features)
- [Dependencies](#dependencies)
- [Installation and Running](#installation-and-running)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Description

BalanceReader is a Spring Boot microservice that:

- Connects to a shared database (MySQL in this example) to read transactions from the `TRANSACTIONS` table.
- Tracks account balances for a specific bank routing number.
- Exposes a REST API to retrieve account balances for authenticated users.
- Includes a liveness probe endpoint for health checks.

## Features

- **Transaction Processing:** Continuously reads new transactions from the `TRANSACTIONS` table and updates the corresponding account balances in memory.
- **Caching:** Leverages Guava's LoadingCache to store and retrieve account balances efficiently.
- **Authentication:** Authenticates requests using JSON Web Tokens (JWTs) and verifies user access to accounts.
- **Metrics:** Exposes metrics via Stackdriver (configurable) for monitoring and observability.
- **Liveness and Readiness Probes:** Supports liveness and readiness probes for container orchestration platforms.

## Dependencies

- Spring Boot
- Spring Data JPA
- MySQL Connector/J
- JWT libraries (Auth0)
- Google Cloud Logging
- Stackdriver Metrics (optional)

## Installation and Running

1. **Clone the repository:**
   ```bash
   git clone https://github.com/google/cloud-samples/
   ```

2. **Build the application:**
   ```bash
   cd cloud-samples/java/anthos/samples/bankofanthos/balancereader
   mvn clean package
   ```

3. **Set environment variables:**
   - `VERSION`: The service version (e.g., 1.0.0)
   - `PORT`: The port the service will listen on (e.g., 8080)
   - `LOCAL_ROUTING_NUM`: The bank routing number for the balances this service tracks (e.g., 123456789)
   - `PUB_KEY_PATH`: The path to the public key file used for JWT verification (e.g., /path/to/key.pem)
   - `SPRING_DATASOURCE_URL`: The connection string for the MySQL database (e.g., jdbc:mysql://localhost:3306/transactions)
   - `SPRING_DATASOURCE_USERNAME`: The database username (e.g., user)
   - `SPRING_DATASOURCE_PASSWORD`: The database password (e.g., password)
   - `ENABLE_TRACING`: Enable or disable tracing (e.g., true/false)
   - `ENABLE_METRICS`: Enable or disable Stackdriver metrics (e.g., true/false)
   - `HOSTNAME`: The hostname of the pod.  This environment variable is injected by Kubernetes.
   - `NAMESPACE`: The namespace of the pod.  This environment variable is injected by Kubernetes.

4. **Run the application:**
   ```bash
   mvn spring-boot:run
   ```

## Testing

- **Unit Tests:** Run `mvn test` to execute the unit tests.
- **Integration Tests:**  Integration tests are not currently included.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a branch for your changes.
3. Make your changes and write tests.
4. Submit a pull request.

Please refer to the [Contributor's Guide](https://github.com/google/cloud-samples/blob/main/CONTRIBUTING.md) for more information.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.
