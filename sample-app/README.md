# Balance Reader

This repository contains the source code for a sample microservice, the Balance Reader, designed to track and provide balances for user accounts. This service demonstrates a basic example of how to build a microservice on Google Cloud, using tools like Spring Boot and SQL for data storage.

## Features

* **Balance Retrieval:**  The Balance Reader provides a REST API endpoint to fetch the current balance for a given account ID.
* **Authentication:** The API enforces authentication using JSON Web Tokens (JWT) to ensure authorized access to account balances.
* **Transaction Processing:** The service listens to a simulated transaction ledger (represented by a database table) and updates its internal cache with balance changes.
* **Metrics and Logging:** Built-in instrumentation provides metrics and logging for monitoring the service's health and performance.
* **Deployment to Kubernetes:** Designed for deployment on Kubernetes, the service includes configuration for health checks and container resource labels.

## Installation

1. **Prerequisites:** 
   * Java Development Kit (JDK) 11 or later
   * Maven
   * Google Cloud SDK
   * kubectl
   * A Google Cloud project

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/GoogleCloudPlatform/microservices-demo.git
   cd microservices-demo/sample-app
   ```

3. **Build the Application:**
   ```bash
   mvn clean package
   ```

## Deployment

1. **Create a Kubernetes Cluster:** 
   * Follow the instructions in the Google Cloud documentation to create a Kubernetes cluster. 
   * You can choose either a Google Kubernetes Engine (GKE) or a Google Anthos cluster.

2. **Configure the Environment Variables:**
   * Before deploying, you need to set the following environment variables:

     * **VERSION:** The version of your application.
     * **PORT:** The port on which the application will listen.
     * **LOCAL_ROUTING_NUM:** The routing number of your simulated bank.
     * **PUB_KEY_PATH:** The path to the public key used for JWT verification.
     * **SPRING_DATASOURCE_URL:** The connection string for the database.
     * **SPRING_DATASOURCE_USERNAME:** The database username.
     * **SPRING_DATASOURCE_PASSWORD:** The database password.
     * **ENABLE_TRACING:** Set to true to enable distributed tracing using OpenTelemetry.

3. **Deploy the Application:**
   * Use the `kubectl` command to deploy the application to your Kubernetes cluster. Here is an example deployment using a `Deployment` and a `Service`:
     ```yaml
     apiVersion: apps/v1
     kind: Deployment
     metadata:
       name: balance-reader
     spec:
       replicas: 1
       selector:
         matchLabels:
           app: balance-reader
       template:
         metadata:
           labels:
             app: balance-reader
         spec:
           containers:
           - name: balance-reader
             image: gcr.io/<PROJECT_ID>/balance-reader:latest
             ports:
             - containerPort: 8080
             env:
               - name: VERSION
                 value: "1.0.0"
               - name: PORT
                 value: "8080"
               - name: LOCAL_ROUTING_NUM
                 value: "123456789" 
               - name: PUB_KEY_PATH
                 value: "/path/to/public/key" 
               - name: SPRING_DATASOURCE_URL
                 value: "jdbc:mysql://<DB_HOST>:<DB_PORT>/<DB_NAME>" 
               - name: SPRING_DATASOURCE_USERNAME
                 value: "<DB_USER>" 
               - name: SPRING_DATASOURCE_PASSWORD
                 value: "<DB_PASSWORD>" 
               - name: ENABLE_TRACING
                 value: "true" 
             resources:
               requests:
                 cpu: 100m
                 memory: 128Mi
               limits:
                 cpu: 500m
                 memory: 512Mi
     ---
     apiVersion: v1
     kind: Service
     metadata:
       name: balance-reader
     spec:
       selector:
         app: balance-reader
       ports:
       - protocol: TCP
         port: 80
         targetPort: 8080
     ```

4. **Access the Application:**
   * Once deployed, you can access the application's REST API endpoint through your cluster's load balancer URL.

## Configuration

* **log4j2.xml:** Configuration for logging using Log4j2.
* **banner.txt:** Custom banner displayed when the application starts.
* **application.properties:** Spring Boot application properties.

## Architecture

The Balance Reader application is structured as follows:

* **BalanceReaderController:**  Handles HTTP requests to the REST API.
* **TransactionRepository:** Defines database interactions for retrieving and saving transactions.
* **LedgerReader:** A background thread that polls the transaction ledger database for new transactions.
* **BalanceCache:** A local cache to store account balances, reducing database queries.
* **JWTVerifierGenerator:** Generates a JWT verifier for authentication.
* **Transaction:** A Java class representing a transaction.

## Contributing

Contributions are welcome! Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

## License

This project is licensed under the Apache 2.0 License.

## Contact

For any questions or issues, please open an issue on this GitHub repository.
