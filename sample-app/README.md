# BalanceReader - A Microservice for Tracking Bank Account Balances

## Table of Contents

- [Description](#description)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Setup and Running the Application](#setup-and-running-the-application)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Description

BalanceReader is a microservice responsible for tracking and retrieving bank account balances for a specific bank routing number. It leverages a database to store transactions, and uses a cache to optimize balance retrieval. The service interacts with an external ledger to receive transaction updates in real-time, ensuring the balance information remains up-to-date.

## Architecture

The BalanceReader service is built on the Spring Boot framework and utilizes several key components:

- **RESTful API:** Exposes endpoints for retrieving account balances based on the provided account ID.
- **Transaction Repository:** A database layer responsible for storing and querying transactions.
- **Balance Cache:** A cache mechanism for improving performance by storing frequently accessed account balances.
- **Ledger Reader:** A component that listens for new transactions from an external ledger and updates the cache accordingly.
- **Authentication:** Utilizes JSON Web Tokens (JWT) for user authentication and authorization.
- **Metrics:** Collects metrics on performance and cache usage using Micrometer and exports them to Stackdriver.
- **Logging:** Uses Log4j2 for logging messages with configurable log levels.

## Prerequisites

- Java Development Kit (JDK) 11 or later
- Apache Maven 3.6.x or later
- Docker
- Google Cloud Platform (GCP) account with a project
- gcloud SDK installed and configured

## Setup and Running the Application

### 1. Configure GCP Project

- **Create a GCP project:** Navigate to the GCP console and create a new project.
- **Enable Cloud SQL:** Enable the Cloud SQL API in your project.
- **Create a Cloud SQL instance:** Create a new Cloud SQL instance using PostgreSQL or MySQL.
- **Create a database and user:**  Create a new database and a user with appropriate permissions to access the database within your Cloud SQL instance.
- **Enable Stackdriver Monitoring:** Enable Stackdriver Monitoring in your GCP project.

### 2. Configure Environment Variables

- **Set up environment variables:** Export the required environment variables as follows:

```bash
export VERSION="v1.0.0"
export PORT=8080
export LOCAL_ROUTING_NUM="123456789"
export PUB_KEY_PATH="/path/to/public_key.pem"
export SPRING_DATASOURCE_URL="jdbc:postgresql://<your-cloud-sql-instance-connection-string>"
export SPRING_DATASOURCE_USERNAME="<your-database-username>"
export SPRING_DATASOURCE_PASSWORD="<your-database-password>"
export ENABLE_TRACING=true # Set to false to disable tracing
export ENABLE_METRICS=true # Set to false to disable metrics
```

- Replace placeholders with actual values.

### 3. Build and Run the Application

- **Build the application:**
  ```bash
  mvn clean install
  ```
- **Run the application locally:**
  ```bash
  mvn spring-boot:run
  ```
- **Run the application using Docker:**
  ```bash
  docker build -t balance-reader .
  docker run -p 8080:8080 -e VERSION="v1.0.0" -e PORT=8080 -e LOCAL_ROUTING_NUM="123456789" -e PUB_KEY_PATH="/path/to/public_key.pem" -e SPRING_DATASOURCE_URL="jdbc:postgresql://<your-cloud-sql-instance-connection-string>" -e SPRING_DATASOURCE_USERNAME="<your-database-username>" -e SPRING_DATASOURCE_PASSWORD="<your-database-password>" -e ENABLE_TRACING=true -e ENABLE_METRICS=true balance-reader
  ```

## Usage

Once the BalanceReader service is running, you can interact with it using the following endpoints:

- **`/version`:** Retrieves the service version.
- **`/ready`:** Checks the readiness of the service.
- **`/healthy`:** Checks the health of the service.
- **`/balances/{accountId}`:** Retrieves the balance for the specified account ID. Requires a valid JWT bearer token in the Authorization header.

## Contributing

We welcome contributions to the BalanceReader service! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Commit your changes and push them to your fork.
4. Submit a pull request to the main repository.

Please adhere to our coding style guide and ensure your code passes all tests.

## License

BalanceReader is released under the Apache 2.0 License.

## Contact

For any questions or feedback, feel free to:

- Open an issue on the GitHub repository.
