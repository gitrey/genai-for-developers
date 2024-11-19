# Balance Reader Service

## Description

This repository contains the source code for the Balance Reader service. It's a microservice that provides a simple API to retrieve the balance of a user's bank account. This service is designed to be deployed to a Kubernetes cluster and leverages various features of the Google Cloud Platform.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
- [Deployment](#deployment)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features

The Balance Reader service offers the following features:

- **Account Balance Retrieval:** Retrieves the current balance of an account based on user authentication.
- **JWT Authentication:** Uses JSON Web Tokens (JWT) to authenticate requests and authorize access to account information.
- **Transaction Processing:** Listens for new transactions from a centralized ledger and updates account balances accordingly.
- **Caching:** Utilizes a local cache to improve performance and reduce database load.
- **Metrics and Monitoring:** Integrates with Google Cloud Monitoring to track service performance, health, and resource utilization.

## Prerequisites

Before you begin, ensure you have the following:

- **Google Cloud Platform (GCP) Account:** A GCP account with the necessary permissions to create and manage resources.
- **Kubernetes Cluster:** A Kubernetes cluster running in GCP, either a Google Kubernetes Engine (GKE) cluster or Anthos on Bare Metal.
- **kubectl:** The Kubernetes command-line interface.
- **Docker:** The Docker containerization platform.
- **Go:** The Go programming language, required for building the ledger service.

## Architecture

The Balance Reader service consists of the following key components:

- **Balance Reader Microservice:** The main application responsible for providing the balance retrieval API.
- **Transaction Repository:** A database that stores transaction records. This could be a PostgreSQL or MySQL database.
- **Ledger Service:** A separate microservice that acts as a centralized ledger, receiving new transactions from external sources.
- **Authentication Service:** An authentication service (not included in this repository) responsible for issuing and verifying JWTs.
- **Google Cloud Monitoring:** Used to monitor the health and performance of the Balance Reader service.

## Getting Started

1. **Clone this repository:**

```bash
git clone https://github.com/GoogleCloudPlatform/microservices-demo
```

2. **Navigate to the Balance Reader project:**

```bash
cd microservices-demo/sample-app/
```

3. **Configure the application properties:**

-   **`application.properties`:** This file contains various configuration settings for the service, including database connection information, port number, and other parameters. 
-   **Environment Variables:** The application also uses environment variables to configure settings, such as the `PORT` and `ENABLE_TRACING`. Make sure to set these environment variables appropriately for your deployment environment. 

4. **Build the project:**

```bash
./mvnw clean install
```

5. **Generate a JWT verifier:**

```bash
go run ../ledger/generate-verifier.go -path "../sample-app/src/main/resources/pubkey.pem"
```

This step generates the `pubkey.pem` file which is needed for JWT authentication in `sample-app`.

## Deployment

To deploy the Balance Reader service, follow these steps:

1. **Create a Kubernetes manifest for the application:**

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
        image: gcr.io/YOUR_PROJECT_ID/balance-reader
        ports:
        - containerPort: 8080
        env:
        - name: PORT
          value: "8080"
        - name: ENABLE_TRACING
          value: "true"
        # ...other environment variables
```

2. **Deploy the manifest to your Kubernetes cluster:**

```bash
kubectl apply -f deployment.yaml
```

3. **Expose the service:**

```bash
kubectl expose deployment balance-reader --type=LoadBalancer --port=8080 --target-port=8080
```

## Testing

1. **Create a test account in the database:**

```sql
INSERT INTO TRANSACTIONS (FROM_ACCT, FROM_ROUTE, TO_ACCT, TO_ROUTE, AMOUNT)
VALUES ('1234567890', '123456789', '1234567890', '123456789', 10000);
```

2. **Retrieve the balance for the test account:**

```bash
curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhenQiOiIxMjM0NTY3ODkwIn0.R80c0-0J3a8y0G-F41r9m276c7M3bW2_5ZqL23084I" http://YOUR_BALANCE_READER_SERVICE_IP:8080/balances/1234567890
```

## Contributing

Contributions are welcome! To contribute, please follow these steps:

1. **Fork the repository.**
2. **Create a new branch for your changes.**
3. **Make your changes and test them thoroughly.**
4. **Submit a pull request with a clear description of your changes.**

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgements

This project is heavily inspired by the Google Cloud Platform Microservices Demo, and built upon the code and examples shared in that project.
