## BalanceReader: A Microservice for Tracking Bank Balances

**[Image of BalanceReader logo]**

### Description

BalanceReader is a lightweight microservice designed to track account balances in real-time. This application leverages a distributed ledger to maintain a consistent view of account balances across multiple instances. It incorporates features such as:

- **Real-time Balance Updates:**  Keeps account balances current by reacting to new transactions from a shared transaction ledger.
- **JWT Authentication:** Securely verifies user authentication through JWT tokens to ensure authorized access to account balances.
- **Caching:** Utilizes Guava cache to efficiently store and retrieve account balances, minimizing database queries and improving performance.
- **Metrics and Observability:** Enables monitoring of key metrics and logs for improved observability and troubleshooting.
- **Kubernetes-Friendly Deployment:** Configured for seamless deployment and scaling within a Kubernetes environment.


### Table of Contents

* **Description**
* **Features**
* **Installation**
* **Usage**
* **Contributing**
* **License**
* **Contact**

### Features

* **Real-time Balance Updates:**
    * Continuously monitors a transaction ledger for new transactions.
    * Updates account balances in the cache based on incoming transactions.
    * Provides a consistent and accurate view of balances across all instances.
* **JWT Authentication:**
    * Enforces secure access to account balances by verifying JWT tokens.
    * Ensures only authorized users can retrieve sensitive balance information.
* **Caching:**
    * Leverages Guava cache to store account balances for efficient retrieval.
    * Minimizes database queries, reducing latency and improving overall performance.
    * Enables scaling of the service by distributing cache instances.
* **Metrics and Observability:**
    * Exports key metrics to Stackdriver for monitoring and insights.
    * Logs essential events for troubleshooting and analysis.
    * Enables effective monitoring of service health and performance.
* **Kubernetes-Friendly Deployment:**
    * Designed for easy deployment and scaling within a Kubernetes environment.
    * Leverages environment variables for configuration and simplifies management.
    * Integrates seamlessly with Kubernetes features for efficient operation.

### Installation

1. **Prerequisites:**
   - Java Development Kit (JDK) 11+
   - Maven
   - Google Cloud SDK
   - Kubernetes Cluster (optional)

2. **Clone the Repository:**

   ```bash
   git clone https://github.com/GoogleCloudPlatform/microservices-demo
   cd microservices-demo/sample-app
   ```

3. **Build the Application:**

   ```bash
   mvn clean install
   ```

4. **Configure Environment Variables:**

   - Set the necessary environment variables for database connection, JWT authentication, and other settings. Refer to `application.properties` for configuration details.

   - **For Kubernetes deployment:**

     - Configure a Kubernetes secret with the required environment variables.
     - Update the `deployment.yaml` file to use the secret.

### Usage

1. **Run the Application Locally:**

   ```bash
   mvn spring-boot:run
   ```

2. **Access the API:**

   - Use `curl` or a REST client to make requests to the BalanceReader API.
   - Refer to the `src/main/java/anthos/samples/bankofanthos/balancereader/BalanceReaderController.java` for API endpoints.

3. **Deploy to Kubernetes:**

   ```bash
   kubectl apply -f deployment.yaml
   ```

### Contributing

We welcome contributions to BalanceReader! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and ensure they adhere to the code style guide.
4. Write comprehensive tests for your changes.
5. Submit a pull request with a clear description of your contributions.

### License

BalanceReader is licensed under the Apache 2.0 License.

### Contact

For any questions or support, please contact us:

* **GitHub:** [Link to GitHub repository]

We value your feedback and suggestions to help us improve BalanceReader and make it a robust and reliable solution for distributed balance management.
