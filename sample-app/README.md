## Sample Bank of Anthos - Balance Reader Service

This directory contains the source code for the Balance Reader service, which forms part of the Sample Bank of Anthos demo application. This microservice allows the retrieval of account balances for authenticated users.

## Architecture

The Balance Reader service interacts with the following components:

* **Transaction Ledger:** An external database storing all transactions within the bank. The Balance Reader service subscribes to updates in the ledger to maintain an up-to-date view of account balances.
* **Authentication Service:** Provides authentication and authorization mechanisms for accessing account balances. JWT tokens are used to authenticate users and validate their access permissions.
* **Metrics and Logging:** Implements monitoring and logging functionalities using Stackdriver and Log4j, respectively, to track service performance and troubleshoot issues.

## Setup and Configuration

**Requirements:**

* **Java 11+**:  Make sure you have a compatible Java Development Kit (JDK) installed.
* **Maven 3+**:  Ensure Maven is installed for project build and dependency management.
* **Google Cloud SDK**:  Required for interacting with Google Cloud services like Stackdriver.
* **Kubernetes cluster:**  The Balance Reader service is designed to be deployed within a Kubernetes cluster.

**Configuration:**

* **Environment Variables:**  The service relies on various environment variables for configuration, including database credentials, public key path, and logging level. These variables can be set using Kubernetes configuration files or other means.

**Example Environment Variables:**

```
# DATABASE CREDENTIALS
SPRING_DATASOURCE_URL=jdbc:mysql://mysql:3306/transactions?useSSL=false&allowPublicKeyRetrieval=true
SPRING_DATASOURCE_USERNAME=user
SPRING_DATASOURCE_PASSWORD=password

# AUTHENTICATION CONFIGURATION
PUB_KEY_PATH=/path/to/public/key

# LOGGING
LOG_LEVEL=DEBUG

# METRICS
ENABLE_METRICS=true
```

**Deployment:**

The service can be deployed to a Kubernetes cluster using a Kubernetes YAML file (e.g., deployment.yaml).

## Service Functionality

**Endpoints:**

* **`/version`:** Returns the service version information.
* **`/ready`:** Readiness probe endpoint, used by Kubernetes to determine service readiness.
* **`/healthy`:** Liveness probe endpoint, used by Kubernetes to assess service health.
* **`/balances/{accountId}`:** Retrieves the balance for the specified account after authentication and authorization checks.

**Authentication:**

The `/balances/{accountId}` endpoint requires a valid JWT token to be passed in the `Authorization` header using the `Bearer` scheme. The token is verified against the public key provided in the `PUB_KEY_PATH` environment variable. The token must also contain an `acct` claim that matches the provided `accountId`.

**Transaction Processing:**

The Balance Reader service periodically polls the Transaction Ledger for new transactions. For each transaction, it updates the balance cache to reflect the changes. 

## Monitoring and Logging

The service leverages Stackdriver for monitoring, capturing metrics related to cache usage and service health. Logging is handled by Log4j, providing detailed logs about service operations, including authentication attempts, cache accesses, and ledger updates.

## Further Information

This README provides a basic overview of the Balance Reader service.  For more detailed information and code documentation, refer to the individual source code files.
