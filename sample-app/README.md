# Balance Reader Microservice

This repository contains the source code for the Balance Reader microservice, which retrieves and caches account balances for a simulated banking application.

## Table of Contents

- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Architecture

The Balance Reader microservice is built using the following technologies:

* **Spring Boot**: Framework for building RESTful microservices
* **Java**: Programming language
* **JPA**: Object-relational mapping framework
* **MySQL**: Relational database for storing transactions
* **Guava Cache**: In-memory cache for account balances
* **JWT**: JSON Web Token for user authentication
* **Log4j2**: Logging framework
* **Micrometer**: Metrics collection framework
* **Stackdriver**: Cloud monitoring service for exporting metrics

The microservice implements a REST API endpoint that allows authenticated users to retrieve the current balance for a specific account. It uses a background thread to listen for new transactions from a simulated bank ledger and updates its cache accordingly. 

## Prerequisites

* **Java Development Kit (JDK) 11 or higher**: For compiling and running the application
* **Maven**: For building and packaging the application
* **Docker**: For running the application in a containerized environment
* **Google Cloud Platform (GCP) account**: For deploying the application to GCP and using Stackdriver

## Setup

1. **Clone the repository:**

```bash
git clone https://github.com/google/cloud-samples/tree/main/java/banking-microservices/sample-app
```

2. **Build the application:**

```bash
cd sample-app
mvn clean package
```

3. **Run the application locally**: 
   * **Option 1: Using Maven**

   ```bash
   mvn spring-boot:run
   ```
   * **Option 2: Using Docker**

   ```bash
   docker build -t balance-reader .
   docker run -d -p 8080:8080 balance-reader
   ```

4. **Run the database locally (MySQL):**

   ```bash
   docker run -d --name mysql -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=bankdb -p 3306:3306 mysql:8.0
   ```

5. **Configure application properties:**

   Before running the application, make sure to set the following environment variables in your local system:

   - **VERSION**: Version of the application. This will be used in the version endpoint.
   - **PORT**: Port on which the application will listen.
   - **LOCAL_ROUTING_NUM**: Routing number of the local bank.
   - **PUB_KEY_PATH**: Path to the public key used for JWT verification.
   - **SPRING_DATASOURCE_URL**: URL of the MySQL database.
   - **SPRING_DATASOURCE_USERNAME**: Username for the MySQL database.
   - **SPRING_DATASOURCE_PASSWORD**: Password for the MySQL database.
   - **ENABLE_TRACING**:  Optional. To enable tracing, set to `true`.
   - **ENABLE_METRICS**:  Optional. To enable metrics, set to `true`.
   - **CACHE_SIZE**: Optional. Size of the Guava Cache. Default value is 1000000.
   - **POLL_MS**: Optional. Polling interval for checking new transactions from the ledger. Default value is 100ms.

   **Example:** 

   ```bash
   export VERSION=v1.0.0
   export PORT=8080
   export LOCAL_ROUTING_NUM=123456789
   export PUB_KEY_PATH=/path/to/public_key.pem
   export SPRING_DATASOURCE_URL=jdbc:mysql://localhost:3306/bankdb
   export SPRING_DATASOURCE_USERNAME=root
   export SPRING_DATASOURCE_PASSWORD=password
   export ENABLE_TRACING=true
   export ENABLE_METRICS=true
   export CACHE_SIZE=1000000
   export POLL_MS=100
   ```

## Usage

1. **Start the Balance Reader application.**
2. **Retrieve account balance:** Send a GET request to the `/balances/{accountId}` endpoint with the account ID in the path and a valid JWT token in the Authorization header.

**Example request:**

```bash
curl -H "Authorization: Bearer <JWT_TOKEN>" http://localhost:8080/balances/123456789
```

**Example response:**

```json
10000
```

## Testing

* **Unit tests**: The project includes unit tests for the business logic and controller.
* **Integration tests**: The project includes integration tests that interact with the database.
* **End-to-end tests**:  The project includes end-to-end tests that simulate interactions with the microservice using a mock ledger.

## Contributing

Contributions to the project are welcome. Please submit pull requests with clear descriptions of your changes. 

## License

This project is licensed under the Apache 2.0 License.

##  Notes

* The  project assumes a simulated bank ledger that provides transactions.
*  This code should not be used in a production environment.
*  The application relies on environment variables, and these should be set accordingly.
* The application uses Stackdriver for metrics. Ensure your project is configured to use Stackdriver.
