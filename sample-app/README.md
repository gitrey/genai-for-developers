## Sample Bank of Anthos: Balance Reader

This repository contains a sample microservice, `BalanceReader`, as part of the [Bank of Anthos](https://cloud.google.com/anthos/docs/tutorials/bank-of-anthos) reference architecture. 

**Table of Contents**

- [Description](#description)
- [Architecture](#architecture)
- [Components](#components)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Run the Application](#run-the-application)
- [Deployment](#deployment)
- [Testing](#testing)
- [Cleaning up](#cleaning-up)
- [License](#license)

## Description

The Balance Reader microservice is responsible for maintaining the current balance for each user account. It uses a cache to store balances, and a background thread to monitor a shared ledger for new transactions. When a transaction affecting an account in the Balance Reader's bank is detected, the balance in the cache is updated. 

## Architecture

This microservice uses the following technologies:

* **Spring Boot:**  Provides a framework for building a RESTful service.
* **Google Cloud SQL:**  Stores transactions in a relational database.
* **Guava Cache:**  Provides a simple in-memory cache for account balances.
* **JWT Authentication:**  Validates user authentication tokens to ensure authorized access.
* **Micrometer:** Exposes metrics and tracing information.

## Components

The `BalanceReader` microservice consists of the following components:

* **BalanceReaderController:** Handles requests to retrieve account balances.
* **BalanceCache:** Implements a Guava cache to store and retrieve account balances.
* **TransactionRepository:** Interface to interact with the `Transactions` database table.
* **LedgerReader:** Monitors the shared ledger for new transactions and updates the cache accordingly.
* **JWTVerifierGenerator:** Generates a JWT verifier to authenticate requests.
* **Transaction:** Represents a transaction between accounts.

## Prerequisites

* **Google Cloud Project:** You'll need a Google Cloud Project with the following services enabled:
    * Google Cloud SQL
    * Cloud Run
    * Cloud Logging
    * Cloud Monitoring
* **Cloud SDK:** The Google Cloud SDK must be installed on your machine and configured with your Google Cloud Project.
* **Docker:** Docker needs to be installed and running.

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/GoogleCloudPlatform/microservices-demo.git
   cd microservices-demo/sample-app
   ```

2. **Build the Docker image:**

   ```bash
   docker build -t balance-reader .
   ```

## Run the Application

1. **Start the application locally:**

   ```bash
   docker run -d --name balance-reader -p 8080:8080 balance-reader
   ```

2. **Access the service:**

   You can now access the Balance Reader service using your browser or a REST client at: `http://localhost:8080`

## Deployment

1. **Deploy to Cloud Run:**

   ```bash
   gcloud run deploy balance-reader --image balance-reader --platform managed --region us-central1 --allow-unauthenticated
   ```

2. **Access the service:**

   You can now access the deployed Balance Reader service at the URL provided in the output of the deployment command.

## Testing

* **Integration Tests:** The `BalanceReader` service comes with integration tests that you can run to ensure the application is working correctly.

   ```bash
   ./mvnw clean install
   ```

* **End-to-End Tests:** You can use the provided `curl` commands in the `test` directory to interact with the deployed service and verify its functionality.

## Cleaning up

1. **Delete the Cloud Run service:**

   ```bash
   gcloud run services delete balance-reader --region us-central1
   ```

2. **Remove the Docker image:**

   ```bash
   docker image rm balance-reader
   ```

3. **Remove the container:**

   ```bash
   docker container rm balance-reader
   ```

## License

This project is licensed under the Apache 2.0 License.
