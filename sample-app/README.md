## Balance Reader - README

This repository contains the source code for the Balance Reader microservice, a key component of the Bank of Anthos application. This service retrieves account balances for authenticated users, demonstrating the use of JWT authentication and cache to improve performance.

### Description

The Balance Reader service is responsible for:

- **Retrieving account balances:** The service fetches the current balance for a given user account.
- **JWT authentication:** It verifies incoming JWT tokens to ensure authorized access to account information.
- **Caching:** It maintains a cache of account balances to reduce the number of database queries and improve response times.
- **Transaction processing:** It listens to a ledger for new transactions and updates the cache accordingly.

### Features

- **REST API:** Exposes endpoints for retrieving balances and health checks.
- **JWT authentication:** Securely verifies user identity using JWT tokens.
- **Guava Cache:** Efficiently caches account balances to improve performance.
- **Spring Boot:** Provides a robust framework for building microservices.
- **Stackdriver Monitoring:** Exports metrics to Stackdriver for monitoring and analysis.
- **Kubernetes readiness and liveness probes:** Ensures the health and availability of the service within a Kubernetes cluster.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/GoogleCloudPlatform/microservices-demo.git
   cd microservices-demo/sample-app/balancereader
   ```
2. **Set environment variables:**
   - `VERSION`: The version of the service.
   - `PORT`: The port for the service to listen on.
   - `LOCAL_ROUTING_NUM`: The routing number of the local bank.
   - `PUB_KEY_PATH`: The path to the public key used for JWT verification.
   - `SPRING_DATASOURCE_URL`: The URL of the database containing transactions.
   - `SPRING_DATASOURCE_USERNAME`: The username for the database.
   - `SPRING_DATASOURCE_PASSWORD`: The password for the database.
   - `ENABLE_METRICS`: (Optional) Set to `false` to disable Stackdriver metrics export.
3. **Build the project:**
   ```bash
   mvn clean package
   ```

### Usage

1. **Deploy the service:**  Deploy the built JAR file to a Kubernetes cluster.
2. **Access the API:**
   - **Get balance:**
     ```bash
     curl -H "Authorization: Bearer <jwt-token>" http://<service-host>:<service-port>/balances/<account-id>
     ```
   - **Version endpoint:**
     ```bash
     curl http://<service-host>:<service-port>/version
     ```
   - **Readiness probe:**
     ```bash
     curl http://<service-host>:<service-port>/ready
     ```
   - **Liveness probe:**
     ```bash
     curl http://<service-host>:<service-port>/healthy
     ```

### Contributing

Contributions are welcome! To contribute, please follow these steps:

1. **Fork the repository.**
2. **Create a new branch** for your feature or bug fix.
3. **Make your changes** and ensure they follow the existing code style.
4. **Test your changes** thoroughly.
5. **Submit a pull request** for review.

### License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for more information.

### Contact

For any questions or feedback, please contact the project maintainers:

- **GitHub:** [https://github.com/GoogleCloudPlatform/microservices-demo](https://github.com/GoogleCloudPlatform/microservices-demo)

### Additional Information

- This service is designed to work with the Bank of Anthos microservices demo application.
- The `sample-app` directory contains the complete application code, including the Balance Reader.
- The `pom.xml` file specifies the dependencies and configuration for the project.
- The project uses Java and Spring Boot as its primary technologies.

This README file provides a comprehensive overview of the Balance Reader service, including its purpose, features, usage, and contribution guidelines.
