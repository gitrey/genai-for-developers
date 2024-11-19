## BalanceReader: A Microservice for Account Balance Tracking

This repository contains the source code for BalanceReader, a microservice designed to track account balances in a simulated banking system. BalanceReader leverages a combination of Spring Boot, Java, and Google Cloud technologies to provide a reliable and scalable solution for tracking account balances in real-time.

### Project Structure

The project is organized as follows:

- `src/main/java/anthos/samples/bankofanthos/balancereader`: Contains the Java source code for the BalanceReader microservice.
- `src/main/resources`: Contains configuration files, such as:
  - `log4j2.xml`: Log4j configuration for logging.
  - `banner.txt`: A custom banner displayed at startup.
  - `application.properties`: Spring Boot application configuration.
- `src/test/java/anthos/samples/bankofanthos/balancereader`: Contains unit tests for the BalanceReader microservice.

### Features

- **Real-time Balance Updates:** BalanceReader actively listens for new transactions and updates account balances in real-time.
- **Reliable Data Storage:**  Account balances are stored in a database using Spring Data JPA.
- **Secure Authentication:**  JWT-based authentication is used to verify the identity of clients requesting account balances.
- **Metrics and Monitoring:**  Integrates with Google Cloud Monitoring to track service performance and identify issues.
- **Scalability:**  Designed for horizontal scaling using Kubernetes, ensuring high availability and responsiveness.

### Installation and Setup

1. **Prerequisites:**
    - Java Development Kit (JDK) 11 or higher
    - Maven
    - Google Cloud SDK
    - kubectl

2. **Clone the repository:**
    ```bash
    git clone https://github.com/google/cloud-samples/
    ```

3. **Build the project:**
    ```bash
    cd cloud-samples/java/anthos/samples/bankofanthos/balancereader
    mvn clean package
    ```

4. **Deploy to Kubernetes:**
    - **Create a Kubernetes cluster:** If you don't have one, create a cluster using the Google Cloud SDK.
    - **Configure your cluster:** Update the configuration file `k8s/deployment.yaml` with the necessary parameters for your Kubernetes cluster, including:
       - **Namespace:** Set the Kubernetes namespace for deploying the service.
       - **Image:** Ensure the container image is updated to match the image you built in step 3.
       - **Environment Variables:** Update the environment variables in the deployment configuration for your specific setup. 
    - **Deploy the service:**
       ```bash
       kubectl apply -f k8s/deployment.yaml
       ```

### Usage

Once deployed, BalanceReader will be accessible through the following endpoints:

- **`/version`:** Returns the service version.
- **`/ready`:** Returns "ok" if the service is ready to receive requests.
- **`/healthy`:** Returns "ok" if the service is healthy and serving requests.
- **`/balances/{accountId}`:** Returns the balance for the specified account, requiring a valid JWT token in the `Authorization` header.

### Contributing

We welcome contributions to this project! Here's how to get started:

1. **Fork the repository.**
2. **Create a new branch for your feature or fix.**
3. **Make your changes and commit them with clear descriptions.**
4. **Push your changes to your fork.**
5. **Submit a pull request to the main repository.**

Please ensure your code adheres to the project's coding style and follows the contribution guidelines.

### License

This project is licensed under the Apache 2.0 License.

### Contact

For any questions or support, please open an issue on the GitHub repository.

### Notes

- **Environment Variables:**
    - `PORT`: Port number for the service to listen on.
    - `ENABLE_TRACING`: Toggle tracing on/off.
    - `PUB_KEY_PATH`: Path to the public key used for JWT verification.
    - `LOCAL_ROUTING_NUM`: Routing number for the local bank.
    - `VERSION`: Service version string.
    - `SPRING_DATASOURCE_URL`: Database connection URL.
    - `SPRING_DATASOURCE_USERNAME`: Database username.
    - `SPRING_DATASOURCE_PASSWORD`: Database password.
- **Dependencies:**
    - **Google Cloud SDK:** For interacting with Google Cloud services.
    - **Kubernetes:** For container orchestration and deployment.
    - **Spring Boot:** For building a microservice application.
    - **Spring Data JPA:** For accessing the database.
    - **JWT:** For authentication and authorization.
    - **Micrometer:** For monitoring and metrics.
    - **Stackdriver:** For exporting metrics to Google Cloud Monitoring.
    - **Log4j 2:** For logging.

This README provides a comprehensive overview of the BalanceReader project. For more detailed information, refer to the code comments and specific documentation for the libraries and frameworks used.
