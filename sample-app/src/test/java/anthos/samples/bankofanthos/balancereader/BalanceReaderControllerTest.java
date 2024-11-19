## BalanceReader

This repository contains the source code for a Spring Boot application that acts as a balance reader service.

## Description

The `BalanceReader` application retrieves and caches account balances for a bank based on a simulated ledger. The application is designed to be deployed in a containerized environment (like Kubernetes).

## Features

* **Secure Authentication:** Uses JWT authentication to verify user requests.
* **Real-Time Balance Updates:** Monitors a ledger for transactions and updates cached balances accordingly.
* **Caching:** Uses Guava cache for fast balance retrieval.
* **Health Checks:** Implements readiness and liveness probes for health monitoring.
* **Metrics:** Tracks service metrics using Stackdriver for performance monitoring and debugging.
* **Logging:** Uses log4j2 for structured logging.

## Installation

1. **Prerequisites:**
   * Java 11 or higher
   * Maven 3.x
   * Google Cloud SDK (for running on GCP)
2. **Clone the repository:**
   ```bash
   git clone https://github.com/google/cloud-samples/
   ```
3. **Build the project:**
   ```bash
   cd cloud-samples/java/anthos/samples/bankofanthos/balancereader/
   mvn clean package
   ```

## Usage

1. **Set up environment variables:**
   * `VERSION`: Service version string.
   * `PORT`: Port to listen on.
   * `LOCAL_ROUTING_NUM`: Routing number of the bank.
   * `PUB_KEY_PATH`: Path to the public key for JWT verification.
   * `SPRING_DATASOURCE_URL`: Database connection URL.
   * `SPRING_DATASOURCE_USERNAME`: Database username.
   * `SPRING_DATASOURCE_PASSWORD`: Database password.
   * `ENABLE_TRACING`: Toggle to enable/disable tracing (defaults to `false`).
   * `ENABLE_METRICS`: Toggle to enable/disable metrics (defaults to `true`).
   * `CACHE_SIZE`: Maximum size of the balance cache (defaults to `1000000`).
   * `POLL_MS`: Polling interval for ledger updates (defaults to `100`).
2. **Deploy the application:**
   * **Locally:**
     ```bash
     mvn spring-boot:run
     ```
   * **Kubernetes:**
     Follow the deployment instructions in the `kubernetes` directory of the repository.
   * **Cloud Run:**
     Follow the deployment instructions in the `cloud-run` directory of the repository.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure proper documentation.
4. Submit a pull request for review.

## License

This project is licensed under the Apache 2.0 License.

## Contact

For any inquiries or feedback, please open an issue on the repository's GitHub page.
