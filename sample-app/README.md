# BalanceReader Service

## Description

This service is a simple microservice that tracks the balance of accounts at a virtual bank. It leverages a database to store transactions and uses a caching mechanism to optimize balance retrieval. The service runs in a Kubernetes environment and uses Spring Boot and Spring Data JPA for backend development.

## Architecture

The service is designed to interact with other services in a larger application. It listens for new transactions and updates the balance for affected accounts. It is also designed to work with a load balancer.

## Key Features

- **Balance Tracking:** Retrieves and updates the balance for each account.
- **Transaction Processing:**  Processes new transactions as they occur.
- **Caching:** Uses a cache to speed up balance retrieval requests.
- **Kubernetes Deployment:** Designed for deployment and scaling in a Kubernetes environment.
- **Health Checks:** Implements readiness and liveness probes for Kubernetes monitoring.
- **Metrics Collection:** Uses Micrometer to collect and export metrics for monitoring and observability.
- **Authentication:** Requires authentication using a JSON Web Token (JWT) for secure access.

## Installation

### Requirements

- Java 11+
- Maven 3+
- Kubernetes Cluster
- Docker

### Installation Steps

1. **Clone the Repository:** Clone the repository to your local machine.

   ```bash
   git clone [repository_url]
   ```

2. **Build the Application:** Build the application using Maven.

   ```bash
   cd balance-reader-service
   mvn clean install
   ```

3. **Configure the Application:** Set the following environment variables in your Kubernetes deployment file:

   - `VERSION`: The service version.
   - `PORT`: The port the service should listen on.
   - `LOCAL_ROUTING_NUM`: The local routing number for the bank.
   - `PUB_KEY_PATH`: The path to the public key for JWT verification.
   - `SPRING_DATASOURCE_URL`: The URL of the database.
   - `SPRING_DATASOURCE_USERNAME`: The username for the database.
   - `SPRING_DATASOURCE_PASSWORD`: The password for the database.

4. **Deploy to Kubernetes:** Deploy the application to your Kubernetes cluster using your preferred method (e.g., kubectl apply).

## Usage

### API Endpoints

- `/version`: Returns the service version.
- `/ready`: Checks if the service is ready to receive requests.
- `/healthy`: Checks if the service is healthy and serving requests.
- `/balances/{accountId}`: Retrieves the balance for the specified account. Requires authentication with a JWT containing the account ID in the `acct` claim.

### Authentication

The service requires authentication with a JWT containing the account ID in the `acct` claim. The JWT is verified using the public key provided in the `PUB_KEY_PATH` environment variable.

### Example Request

```
curl -H 'Authorization: Bearer <your_jwt>' -X GET http://localhost:8080/balances/1234567890
```

## Contributing

Contributions to the BalanceReader service are welcome. To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with clear commit messages.
4. Push your branch to your fork.
5. Submit a pull request to the main repository.

## License

This project is licensed under the Apache 2.0 License.

## Contact

For any questions or feedback, please open an issue on the GitHub repository.
