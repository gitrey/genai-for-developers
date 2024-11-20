## Bank of Anthos - Balance Reader Microservice

This repository contains the source code for a simple microservice that tracks user account balances. The Balance Reader service utilizes a ledger database to get transaction updates and uses a cache to store the account balances locally.

## Table of Contents

- [Architecture](#architecture)
- [Deployment](#deployment)
- [Configuration](#configuration)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Architecture

The Balance Reader microservice is built using Spring Boot and utilizes several key components:

* **JWT Authentication:** Authenticates requests using JSON Web Tokens (JWTs) to verify user identity and access permissions.
* **LoadingCache:**  Leverages Google Guava's LoadingCache to efficiently store and retrieve account balances.
* **Transaction Repository:** Interfaces with a database to access and process transaction records.
* **Ledger Reader:** Continuously polls the database for new transactions and updates the local cache accordingly.

## Deployment

The Balance Reader service can be deployed as a containerized application using Docker and Kubernetes.

**Prerequisites:**

* Docker
* Kubernetes cluster (e.g., Google Kubernetes Engine, Minikube)
* kubectl

**Steps:**

1. Build the Docker image:
```bash
docker build -t balance-reader .
```

2. Push the image to a container registry:
```bash
docker push <registry>/balance-reader
```

3. Create a Kubernetes deployment manifest (e.g., deployment.yaml):
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
        image: <registry>/balance-reader
        ports:
        - containerPort: 8080
```

4. Apply the deployment manifest to your Kubernetes cluster:
```bash
kubectl apply -f deployment.yaml
```

5. Expose the service using a Kubernetes service:
```bash
kubectl expose deployment balance-reader --type=LoadBalancer --port=8080 --target-port=8080
```

6. Get the external IP address of the service and use it to access the Balance Reader API.

## Configuration

The service is configured using environment variables and application.properties file.

**Environment Variables:**

| Variable | Description |
|---|---|
| `VERSION` |  Microservice version. |
| `PORT` |  Microservice port. |
| `LOCAL_ROUTING_NUM` | Routing number for the local bank. |
| `PUB_KEY_PATH` | Path to the public key used for JWT verification. |
| `SPRING_DATASOURCE_URL` | URL for connecting to the ledger database. |
| `SPRING_DATASOURCE_USERNAME` | Username for connecting to the ledger database. |
| `SPRING_DATASOURCE_PASSWORD` | Password for connecting to the ledger database. |
| `CACHE_SIZE` | Maximum size of the balance cache. |
| `POLL_MS` | Polling interval (in milliseconds) for new transactions. |
| `ENABLE_TRACING` | Enables tracing for request handling. |
| `ENABLE_METRICS` | Enables metrics collection and exporting. |

**application.properties:**

* `handlers`: Configuration for logging handlers.
* `spring.main.banner-mode`: Disables the spring boot banner.
* `spring.sleuth.enabled`: Enables or disables tracing.
* `spring.sleuth.sampler.probability`: Sets the probability of sampling requests for tracing.
* `spring.sleuth.web.skipPattern`: Defines patterns for requests to be skipped from tracing.
* `spring.sleuth.log.slf4j.enabled`: Disables logging for tracing information.
* `server.tomcat.mbeanregistry.enabled`: Enables Tomcat metrics collection.
* `spring.jpa.properties.hibernate.generate_statistics`: Enables JPA metrics collection.

## Testing

The Balance Reader service includes unit and integration tests to ensure functionality and code quality.

**Unit Tests:**

* Test individual methods within the service.
* Verify the logic of functions like cache management, transaction processing, and authentication.

**Integration Tests:**

* Test the interaction between the service and the ledger database.
* Verify the functionality of end-to-end flows like retrieving balances or processing transactions.

## Contributing

We welcome contributions! Please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request to the original repository.

## License

This project is licensed under the Apache 2.0 License.

## Contact

For any questions or feedback, please contact the development team.
