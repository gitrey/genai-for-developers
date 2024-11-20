# Balance Reader

This README provides an overview of the Balance Reader microservice, a component of the Bank of Anthos sample application.

## Description

The Balance Reader is a Spring Boot application that provides a REST endpoint for retrieving user account balances. It interacts with a shared database of bank transactions and a JWT-based authentication system to secure access.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Architecture](#architecture)
- [Configuration](#configuration)
- [Installation and Deployment](#installation-and-deployment)
- [Usage](#usage)
- [Metrics](#metrics)
- [Contributing](#contributing)
- [License](#license)

## Features

* **Secure Balance Retrieval:** The service retrieves balances for authenticated users only.
* **Transaction Processing:** The service listens for new transactions and updates the balance cache in real-time.
* **Cache Optimization:** Utilizes a Guava Cache to improve performance and reduce database load.
* **Liveness and Readiness Probes:** Provides health check endpoints for monitoring and automated restart.
* **Metrics and Tracing (optional):** Supports integration with Stackdriver and Zipkin for observability.

## Architecture

The Balance Reader service interacts with other components as follows:

* **Transaction Database:** Stores the history of all bank transactions.
* **JWT Authentication Service:** Provides authentication and authorization for user requests.
* **LedgerReader:** Monitors for new transactions in the shared database.

## Configuration

The following environment variables are used to configure the Balance Reader service:

* **VERSION:**  The version of the service.
* **PORT:** The port the service will listen on.
* **LOCAL_ROUTING_NUM:** The routing number of the bank branch this service is associated with.
* **PUB_KEY_PATH:** The path to the public key used for JWT verification.
* **SPRING_DATASOURCE_URL:** The URL of the database storing bank transactions.
* **SPRING_DATASOURCE_USERNAME:** The username for accessing the database.
* **SPRING_DATASOURCE_PASSWORD:** The password for accessing the database.
* **ENABLE_TRACING:** (Optional)  Enables/disables tracing using Zipkin.
* **ENABLE_METRICS:** (Optional) Enables/disables exporting metrics to Stackdriver.

## Installation and Deployment

The Balance Reader is built using Spring Boot. To install and deploy it, follow these steps:

1. **Clone the repository:** `git clone https://github.com/GoogleCloudPlatform/microservices-demo`
2. **Build the application:** `cd microservices-demo/sample-app && mvn clean install`
3. **Create a Kubernetes deployment:** Refer to the [deployment instructions](https://github.com/GoogleCloudPlatform/microservices-demo/tree/master/sample-app#deployment) for the complete Bank of Anthos application.

## Usage

Once deployed, the Balance Reader exposes the following endpoint:

* `/balances/{accountId}`: Retrieves the balance of the account with the given ID. This endpoint requires a valid JWT token in the `Authorization` header.

## Metrics

The Balance Reader service can optionally export metrics to Stackdriver. 

To enable metrics export:

* Set the environment variable `ENABLE_METRICS=true`.

## Contributing

Contributions are welcome! Please follow the [contribution guidelines](https://github.com/GoogleCloudPlatform/microservices-demo/blob/master/CONTRIBUTING.md) for submitting pull requests.

## License

The Balance Reader service is licensed under the Apache 2.0 License. 

## Contact

For any questions or feedback, please open an issue on the [Bank of Anthos GitHub repository](https://github.com/GoogleCloudPlatform/microservices-demo).
