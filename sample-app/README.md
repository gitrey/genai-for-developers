# BalanceReader

This repository contains the code for a simple microservice, BalanceReader, that retrieves the current balance of a user's bank account. BalanceReader uses a JWT verifier to authenticate users and a LoadingCache to store account balances in memory. It also listens for incoming transactions from a shared database, updating the cached balances accordingly. 

## Architecture

BalanceReader is a Spring Boot application using the following technologies:

* **Spring Boot:** Framework for creating standalone, production-ready Spring applications.
* **Spring Data JPA:** Simplifies data access with a consistent, JPA-based approach.
* **Guava Cache:** Provides a fast, efficient, and thread-safe in-memory cache for account balances.
* **Auth0 JWT:**  Verifies JWT tokens to authenticate user requests.
* **Log4j2:** Used for logging.
* **Micrometer:** Provides instrumentation for collecting and exporting application metrics to Stackdriver.

## Running the application

1. **Prerequisites:**

   * **Google Cloud Project:** You'll need a Google Cloud Project with an enabled Cloud SQL instance and Stackdriver Monitoring.
   * **Docker:** Install Docker to build and run the application container.
   * **Kubernetes:** Install Kubernetes to deploy the container.
   * **kubectl:** Install kubectl to interact with your Kubernetes cluster.
   * **gcloud:** Install gcloud CLI to authenticate with Google Cloud and manage your project.

2. **Setting up the environment variables:**

   * **PUB\_KEY\_PATH:** Path to the public key used for JWT verification.
   * **LOCAL\_ROUTING\_NUM:** The routing number of the local bank branch.
   * **SPRING\_DATASOURCE\_URL:** URL of the Cloud SQL instance hosting the transaction database.
   * **SPRING\_DATASOURCE\_USERNAME:** Username for the Cloud SQL instance.
   * **SPRING\_DATASOURCE\_PASSWORD:** Password for the Cloud SQL instance.
   * **PORT:** The port the application listens on. (Default: 8080)
   * **ENABLE\_TRACING:**  Enable or disable tracing. (Default: off)
   * **VERSION:** The version of the application.
   * **CACHE\_SIZE:** The maximum size of the LoadingCache. (Default: 1000000)
   * **POLL\_MS:** The interval (in milliseconds) between polls to the database for new transactions. (Default: 100)
   * **ENABLE\_METRICS:** Enable or disable metrics collection and export. (Default: on)

   **Example:**

   ```bash
   export PUB_KEY_PATH=/path/to/public_key.pem
   export LOCAL_ROUTING_NUM=123456789
   export SPRING_DATASOURCE_URL=jdbc:mysql://[INSTANCE_NAME]:3306/[DATABASE_NAME]?cloudSqlInstance=[INSTANCE_NAME]
   export SPRING_DATASOURCE_USERNAME=[USER_NAME]
   export SPRING_DATASOURCE_PASSWORD=[PASSWORD]
   export PORT=8080
   export ENABLE_TRACING=true
   export VERSION=v1.0.0
   export CACHE_SIZE=1000000
   export POLL_MS=100
   export ENABLE_METRICS=true
   ```

3. **Building the Docker image:**

   ```bash
   docker build -t balance-reader .
   ```

4. **Deploying to Kubernetes:**

   * Create a Kubernetes deployment configuration file (`deployment.yaml`) with the environment variables set:

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
           image: balance-reader
           ports:
           - containerPort: 8080
           env:
           - name: PUB_KEY_PATH
             value: /path/to/public_key.pem
           - name: LOCAL_ROUTING_NUM
             value: "123456789"
           - name: SPRING_DATASOURCE_URL
             value: "jdbc:mysql://[INSTANCE_NAME]:3306/[DATABASE_NAME]?cloudSqlInstance=[INSTANCE_NAME]"
           - name: SPRING_DATASOURCE_USERNAME
             value: "[USER_NAME]"
           - name: SPRING_DATASOURCE_PASSWORD
             value: "[PASSWORD]"
           - name: PORT
             value: "8080"
           - name: ENABLE_TRACING
             value: "true"
           - name: VERSION
             value: "v1.0.0"
           - name: CACHE_SIZE
             value: "1000000"
           - name: POLL_MS
             value: "100"
           - name: ENABLE_METRICS
             value: "true"
   ```

   * Apply the deployment configuration:

   ```bash
   kubectl apply -f deployment.yaml
   ```

## Usage

Once deployed, BalanceReader will be accessible via a Kubernetes Service. You can access the service using the `kubectl get services` command to retrieve the service's endpoint. 

## Endpoints

* **/version:** Returns the service's version.
* **/ready:** Health check endpoint to confirm readiness.
* **/healthy:** Liveness check endpoint to confirm health.
* **/balances/{accountId}:** Returns the balance of the account specified in the path parameter. Requires a valid JWT token in the `Authorization` header.

## Monitoring and Metrics

BalanceReader uses Micrometer to collect and export application metrics to Stackdriver. These metrics provide insights into the service's performance and health.

## Security

BalanceReader uses JWT authentication to verify user identity and authorization. The JWT verification process uses a public key to ensure token authenticity. 

## Contributing

Contributions are welcome! Please submit a pull request with clear documentation of changes and unit tests.

## License

This project is licensed under the Apache 2.0 License.

## Contact

For questions or support, please reach out to the repository owner or file an issue.
