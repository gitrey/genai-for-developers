## Balance Reader Microservice

This repository contains the source code for a Spring Boot microservice that tracks the balance of user accounts.

### Description

The `balance-reader` microservice is designed to be part of a distributed system for managing banking transactions. It subscribes to a stream of transactions, keeping track of balances for all accounts within its local routing number.  

It features:

* **Caching:** Balances are stored in a local cache to reduce the need for database lookups.
* **Authentication:** Access to account balances is protected by JWT authentication.
* **Metrics:** The service exposes Prometheus metrics for monitoring its performance.
* **Health Checks:** The service provides readiness and liveness probes for monitoring its health.

### Prerequisites

* Java Development Kit (JDK) 11 or higher
* Maven 3.6.x or higher
* Google Cloud SDK
* Kubernetes cluster

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/balance-reader.git
   cd balance-reader
   ```

2. **Build the application:**

   ```bash
   mvn clean package
   ```

3. **Deploy to Kubernetes:**

   This repository includes a `deployment.yaml` file for deploying to a Kubernetes cluster. You will need to modify the file to include your specific cluster and image repository details.

   ```bash
   kubectl apply -f deployment.yaml
   ```

### Configuration

The following environment variables can be used to configure the application:

* **PORT:** The port the application listens on (default: 8080)
* **LOCAL_ROUTING_NUM:** The local routing number the service is responsible for
* **PUB_KEY_PATH:** Path to the public key used for JWT verification
* **SPRING_DATASOURCE_URL:** URL for the database connection
* **SPRING_DATASOURCE_USERNAME:** Username for the database connection
* **SPRING_DATASOURCE_PASSWORD:** Password for the database connection
* **ENABLE_TRACING:** Whether or not to enable tracing (default: false)
* **ENABLE_METRICS:** Whether or not to enable metrics export (default: true)
* **CACHE_SIZE:** Maximum size of the balance cache (default: 1000000)
* **POLL_MS:** Number of milliseconds between polls for new transactions (default: 100)

### Usage

After deploying the microservice, you can access the following endpoints:

* `/version`: Returns the service version.
* `/ready`: Indicates whether the service is ready to receive requests.
* `/healthy`: Indicates whether the service is healthy and serving requests.
* `/balances/{accountId}`: Returns the balance of the specified account. Requires a valid JWT token in the `Authorization` header.

### Contributing

Contributions are welcome! Please follow the guidelines below:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.

### License

This project is licensed under the Apache 2.0 License. See the LICENSE file for details.

### Contact

If you have any questions or issues, please feel free to open an issue on this repository.
