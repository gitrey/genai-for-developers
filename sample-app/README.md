## Balance Reader README

This repository contains a Spring Boot application called Balance Reader, designed as a microservice to track user account balances within a simulated banking system. The service leverages a database (e.g., PostgreSQL) to store transaction records and provides a REST API for retrieving account balances.

### Table of Contents

* [Architecture](#architecture)
* [Deployment](#deployment)
* [Environment Variables](#environment-variables)
* [API Endpoints](#api-endpoints)
* [Building and Running](#building-and-running)
* [Testing](#testing)
* [Contributing](#contributing)
* [License](#license)

### Architecture

The Balance Reader service is built on the following components:

* **Spring Boot:** Provides a framework for building and deploying the microservice.
* **REST API:** Exposes endpoints for retrieving account balances.
* **Transaction Repository:** Manages interactions with the database for storing and retrieving transaction data.
* **Ledger Reader:** Continuously monitors the transaction database for new transactions and updates the cache accordingly.
* **Cache:** A Guava cache stores account balances for efficient retrieval.
* **JWT Authentication:** Uses JWT tokens for secure authentication and authorization.
* **Stackdriver Monitoring:** Integrates with Stackdriver to collect and monitor application metrics.

### Deployment

The Balance Reader service can be deployed in various environments, including:

* **Kubernetes:**  The service is designed to run in a Kubernetes cluster, leveraging the benefits of containerization and orchestration.
* **Cloud Run:** A serverless platform that provides automatic scaling and simplifies deployment.

### Environment Variables

The application requires the following environment variables to be set:

* **VERSION:**  Version string for the service.
* **PORT:**  The port on which the service listens for requests.
* **LOCAL_ROUTING_NUM:**  Routing number for the local bank.
* **PUB_KEY_PATH:**  Path to the public key file used for JWT verification.
* **SPRING_DATASOURCE_URL:** URL for connecting to the database.
* **SPRING_DATASOURCE_USERNAME:** Username for the database connection.
* **SPRING_DATASOURCE_PASSWORD:** Password for the database connection.
* **ENABLE_METRICS:** Optional, if set to "false", disables metrics export to Stackdriver. (Defaults to true)
* **POLL_MS:**  Interval (in milliseconds) for the Ledger Reader to poll the database for new transactions (defaults to 100).
* **CACHE_SIZE:**  Maximum size of the account balance cache (defaults to 1,000,000).

### API Endpoints

The Balance Reader service exposes the following REST endpoints:

* **/version:** Returns the service version string.
* **/ready:**  A readiness probe endpoint that returns "ok" if the server is ready to receive requests.
* **/healthy:** A liveness probe endpoint that returns "ok" if the server is healthy and serving requests.
* **/balances/{accountId}:** Retrieves the balance for the specified account. Requires a valid JWT bearer token in the Authorization header.

### Building and Running

1. **Prerequisites:** 
   * Java Development Kit (JDK) 17 or later
   * Maven 3.x
   * Docker

2. **Build:** 
   ```bash
   mvn clean package
   ```

3. **Run Locally:**
   * Set the necessary environment variables as described above.
   * Run the following command:
     ```bash
     mvn spring-boot:run
     ```

4. **Run in Docker:**
   * Build the Docker image:
     ```bash
     mvn jib:build 
     ```
   * Run the Docker image:
     ```bash
     docker run -p 8080:8080 <image-name>
     ```

### Testing

Unit tests are included in the `src/test/java` directory.

To run the tests:

```bash
mvn test
```

### Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository.
2. Create a branch for your feature or bug fix.
3. Make changes and write unit tests.
4. Submit a pull request.

Please adhere to the project's coding style and documentation guidelines.

### License

This project is licensed under the Apache 2.0 License.
