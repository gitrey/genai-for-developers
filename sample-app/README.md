# Bank of Anthos - Balance Reader

This repository contains the source code for the Balance Reader microservice, a component of the Bank of Anthos application.

## Overview

The Balance Reader is responsible for:

- **Maintaining account balances:** The Balance Reader tracks the balance of accounts within its local routing number.
- **Handling incoming transactions:** When new transactions are processed by the ledger, the Balance Reader updates its account balances accordingly.
- **Serving balance queries:** Clients can query the Balance Reader to retrieve the current balance of an account. 
- **Exposing health and version endpoints:** The Balance Reader provides health and version endpoints for monitoring and debugging purposes.

## Architecture

The Balance Reader is a Spring Boot application with the following key components:

- **Spring Boot:** Provides a framework for building RESTful microservices.
- **Spring Data JPA:** Provides an abstraction layer for interacting with the database.
- **Log4j2:** Provides logging capabilities.
- **Micrometer Stackdriver:** Enables exporting metrics to Stackdriver Monitoring.
- **JWT Authentication:**  Verifies JWT tokens for authorization.
- **Guava Cache:**  Caches account balances for improved performance.

## Dependencies

- **Google Cloud SDK:** Required for interacting with Google Cloud services (e.g., Stackdriver Monitoring).
- **Java 11 or higher:** Required for running the application.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/GoogleCloudPlatform/microservices-demo
   ```

2. **Navigate to the Balance Reader directory:**

   ```bash
   cd microservices-demo/sample-app
   ```

3. **Install dependencies:**

   ```bash
   mvn clean install
   ```

## Running the Application

1. **Set environment variables:**

   ```bash
   export VERSION=1.0.0
   export PORT=8080
   export LOCAL_ROUTING_NUM=123456789
   export PUB_KEY_PATH=/path/to/public_key.pem
   export SPRING_DATASOURCE_URL=jdbc:mysql://localhost:3306/bankofanthos
   export SPRING_DATASOURCE_USERNAME=user
   export SPRING_DATASOURCE_PASSWORD=password
   export ENABLE_TRACING=true # or false
   export ENABLE_METRICS=true # or false
   export HOSTNAME=balance-reader-pod-1234567890
   export NAMESPACE=default
   ```

   **Note:** Replace the placeholder values with your actual environment variables.

2. **Start the application:**

   ```bash
   mvn spring-boot:run
   ```

## Usage

The Balance Reader exposes the following endpoints:

- **`/version`:** Returns the service version.
- **`/ready`:** Health endpoint to check if the service is ready to receive requests.
- **`/healthy`:** Liveness endpoint to check if the service is healthy and serving requests.
- **`/balances/{accountId}`:** Returns the balance of the specified account. Requires a valid JWT token in the `Authorization` header.

## Contributing

Contributions are welcome! Please follow the following guidelines:

1. **Fork the repository.**
2. **Create a new branch for your changes.**
3. **Make your changes and commit them with clear and concise messages.**
4. **Push your changes to your fork.**
5. **Submit a pull request to the main repository.**

## License

The Balance Reader is licensed under the Apache 2.0 License.

## Contact

For support, questions, or feedback, please open an issue on the GitHub repository: [link to GitHub repository]

## Additional Notes

- This README provides a high-level overview of the Balance Reader microservice. For more detailed information, please refer to the source code and comments within the code.
- The Balance Reader is designed to be used in conjunction with other components of the Bank of Anthos application, such as the Ledger and Account Management services.
- The Balance Reader is a sample application that demonstrates best practices for building microservices on Google Cloud. It is not intended to be a production-ready solution.
