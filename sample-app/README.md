## Sample Bank of Anthos - Balance Reader

This repository contains a sample microservice that tracks and reads bank account balances from a shared database. This microservice serves as a component of a larger bank application that uses Anthos for deployment and management.

**Project Structure**

- **src/main/java/anthos/samples/bankofanthos/balancereader**: Contains the main application logic and classes.
  - **BalanceCache**: Manages account balance caching using Guava cache.
  - **BalanceReaderApplication**:  Main application class that initializes Spring Boot and sets up the application.
  - **BalanceReaderController**: Defines REST endpoints for retrieving account balances and handling health checks.
  - **JWTVerifierGenerator**: Generates JWT verifier to authenticate users and authorize access to accounts.
  - **LedgerReader**: Continuously reads and processes transactions from the database, updating account balances in cache.
  - **Transaction**: Represents a single transaction in the bank ledger.
  - **TransactionRepository**: Interface defining database operations for transactions.
- **src/main/resources**: Contains configuration files.
  - **application.properties**: Spring Boot application configuration.
  - **banner.txt**: Banner displayed on application startup.
  - **log4j2.xml**: Logging configuration for Log4j2.
- **src/test/java/anthos/samples/bankofanthos/balancereader**: Contains unit and integration tests.
  - **BalanceReaderControllerTest**: Tests the BalanceReaderController class.

**Technologies Used**

- **Spring Boot**: Framework for building REST APIs.
- **Java**: Programming language.
- **Guava Cache**:  In-memory caching library for efficient storage and retrieval of account balances.
- **JWT**: Used for user authentication and authorization.
- **MySQL**: Database for storing transactions and account balances.
- **Micrometer**: Library for instrumenting the application and exporting metrics.
- **Stackdriver**: Google Cloud monitoring and logging service.
- **Log4j2**: Logging library.
- **Mockito**: Mocking library for testing.

**Features**

- **Account Balance Retrieval:** Securely retrieves the current balance for an authenticated user's account.
- **Real-Time Transaction Processing**:  Monitors and updates account balances in real-time based on transactions committed to the database.
- **Caching**: Uses Guava cache to optimize performance for frequently accessed account balances.
- **Health Checks**: Provides readiness and liveness probes for Kubernetes deployments.
- **Metrics Export**: Exports application metrics to Stackdriver for monitoring and analysis.
- **Authentication and Authorization**: Securely authenticates users using JWTs and authorizes access to specific accounts.
- **Transaction Processing**: Continuously polls the database for new transactions and updates account balances accordingly.

**Installation**

1. **Prerequisites:**
   - Java Development Kit (JDK) 11 or later.
   - Maven or Gradle.
   - Google Cloud SDK and a Google Cloud project.
   - MySQL database instance.
2. **Clone the Repository:**
   ```bash
   git clone https://github.com/GoogleCloudPlatform/microservices-demo.git
   cd microservices-demo/sample-app
   ```
3. **Configure Environment Variables:**
   - `VERSION`: The version of the service.
   - `PORT`: The port on which the service will run.
   - `LOCAL_ROUTING_NUM`: The routing number of the local bank.
   - `PUB_KEY_PATH`: Path to the public key for JWT verification.
   - `SPRING_DATASOURCE_URL`: URL of the MySQL database.
   - `SPRING_DATASOURCE_USERNAME`: Username for the MySQL database.
   - `SPRING_DATASOURCE_PASSWORD`: Password for the MySQL database.
   - `ENABLE_TRACING`: Optional, set to `true` to enable tracing.
   - `ENABLE_METRICS`: Optional, set to `false` to disable metric export.
4. **Build the Application:**
   ```bash
   mvn clean package
   ```
5. **Deploy to Kubernetes:**
   - Create a Kubernetes cluster.
   - Create a deployment manifest (`deployment.yaml`) for the application.
   - Apply the manifest to your Kubernetes cluster:
     ```bash
     kubectl apply -f deployment.yaml
     ```

**Usage**

- Once deployed, the balance reader service will be accessible via a public IP address assigned by Kubernetes.
- To retrieve an account balance, send a GET request to the `balances/{accountId}` endpoint.
- The request must include a valid JWT token in the `Authorization` header. The JWT token should contain the account ID in the `acct` claim.
- The response will contain the account balance as a JSON value.

**Contributing**

Contributions are welcome! Please refer to the CONTRIBUTING.md file for guidelines.

**License**

This project is licensed under the Apache 2.0 License. See the LICENSE file for more information.

**Contact**

For any questions or feedback, please contact the Google Cloud Platform team.
