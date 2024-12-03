##  Balance Reader

The Balance Reader microservice is responsible for tracking the bank balance for each user account. It consumes transaction events published to a message queue and updates a cache with the latest balances.  A REST service is exposed for reading account balances, authenticating users using JWT tokens.  

## Table of Contents

- [Description](#description)
- [Architecture](#architecture)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)


## Description

The Balance Reader service offers a simple and efficient way to track account balances for a bank system. It relies on a shared transaction ledger to maintain a consistent view of account activity. The service is designed for reliability and scalability, utilizing a cache to optimize balance retrieval and a background thread to process transaction events in real-time.

## Architecture

The Balance Reader service is implemented using Spring Boot and leverages the following key components:

- **REST API:** Exposes an endpoint to read account balances, secured with JWT authentication.
- **Cache:**  Uses a Guava cache to store account balances, providing fast retrieval.
- **Transaction Processor:** Consumes transaction events from a message queue and updates the cache. 
- **Database Connection:** Connects to a database to retrieve and store transaction data.
- **Metric Reporting:** Uses Stackdriver for monitoring and logging.
- **JWT Authentication:** Uses JWT tokens for user authentication.

## Features

- **Real-time Balance Updates:** The service tracks changes to account balances in real-time as transactions are processed.
- **Fast Balance Retrieval:** The cache allows for quick retrieval of account balances, enhancing performance.
- **Scalability:** The service is designed to scale horizontally for handling high transaction volumes.
- **Robustness:** Error handling mechanisms are implemented to ensure resilience and high availability.
- **Secure Authentication:** JWT tokens are used for user authentication, ensuring secure access to account information.

## Installation

1. **Prerequisites:**
   - Java 17 or higher
   - Maven 3.6.3 or higher
   - Docker
   -  A Postgresql database.

2. **Clone the repository:**

   ```bash
   git clone https://github.com/GoogleCloudPlatform/microservices-demo.git
   cd microservices-demo/sample-app/balancereader
   ```

3. **Build the project:**
   ```bash
   mvn clean package
   ```

4. **Run the application:**

   ```bash
   mvn spring-boot:run
   ```

## Configuration

The Balance Reader service is configured using environment variables:

- **VERSION:**  Service version (e.g., "1.0").
- **PORT:** The service listening port (e.g., "8080").
- **LOCAL_ROUTING_NUM:** Routing number for the bank (e.g., "123456789").
- **PUB_KEY_PATH:** Path to the public key used for JWT verification (e.g., "path/to/public_key.pem").
- **SPRING_DATASOURCE_URL:** URL of the database (e.g., "jdbc:postgresql://hostname:port/database_name").
- **SPRING_DATASOURCE_USERNAME:** Database username.
- **SPRING_DATASOURCE_PASSWORD:** Database password.
- **CACHE_SIZE:** Maximum size of the cache (default: 1000000).
- **POLL_MS:** Time interval between database polls (default: 100 milliseconds).
- **ENABLE_METRICS:** Enables/disables Stackdriver metric export (default: true).

## Usage

1. **Start the application:**
    - Use the commands from the Installation section.

2. **Test the endpoint:**

    - **Version:**
        ```bash
        curl http://localhost:8080/version
        ```
    - **Readiness Probe:**
        ```bash
        curl http://localhost:8080/ready
        ```
    - **Liveness Probe:**
        ```bash
        curl http://localhost:8080/healthy
        ```
    - **Balance:**
        ```bash
        curl -H "Authorization: Bearer <jwt_token>" http://localhost:8080/balances/<account_id>
        ``` 
       Replace `<jwt_token>` with a valid JWT token and `<account_id>` with the desired account ID.

## Testing

1. **Unit Tests:**
   - Run unit tests with the command:
     ```bash
     mvn test
     ```
2. **Integration Tests:**
   - Integration tests are not provided in this sample.

## Contributing

We welcome contributions! To contribute to this project, please follow these steps:

1. **Fork the repository:**
   - Create a fork of the repository on GitHub.
2. **Create a new branch:**
   - Create a new branch for your feature or bug fix.
3. **Make your changes:**
   - Commit your changes with clear commit messages.
4. **Push your branch:**
   - Push your branch to your fork.
5. **Submit a pull request:**
   - Submit a pull request to the original repository.

## License

This project is licensed under the Apache 2.0 License. See the `LICENSE` file for more information.

## Contact

For any questions or issues, please contact us by opening an issue on the GitHub repository: [link to GitHub repository]
