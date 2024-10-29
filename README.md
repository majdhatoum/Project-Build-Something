# Build Something Project: User/Product Management System

## Description
This is a microservice-based application that allows users to manage products and users through a web interface. The application utilizes a MongoDB database to store and retrieve data, providing an efficient and scalable solution for user and product management. The application is built using Flask for the backend services and React for the frontend, deployed on a Kubernetes cluster.

## Features
- **User Management**: Add, view, and remove users.
- **Product Management**: Add, view, and remove products.
- **Persistent Data Storage**: Uses MongoDB as a backend database.
- **Microservices Architecture**: Each component (user service, product service, frontend) runs as a separate service in Kubernetes.
- **Responsive Web Interface**: Built with React for a dynamic user experience.

## Architecture
The application follows a microservices architecture consisting of the following components:
- **Frontend Service**: Handles user interactions and communicates with the backend services.
- **User Service**: Manages user-related operations (CRUD).
- **Product Service**: Manages product-related operations (CRUD).
- **MongoDB**: A NoSQL database used for persistent storage of user and product data.

The communication between services is done using REST APIs, and the application is deployed using Kubernetes with NodePort services for external access.

## Technologies Used
- **Backend**: Python, Flask
- **Frontend**: JavaScript, React
- **Database**: MongoDB
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **Version Control**: GitHub

## Prerequisites
- **Docker**: Ensure Docker is installed on your machine.
- **Kubernetes**: A local setup using Minikube or any other Kubernetes provider.
- **Node.js**: Required for running the frontend application.

## Getting Started

### Clone the Repository
```bash
git clone https://github.com/majdhatoum/Project-Build-Something.git
cd Project-Build-Something
```

### Set Up MongoDB
Navigate to the `database` directory and apply the MongoDB deployment:
   ```bash
   kubectl apply -f mongo-deployment.yaml
```

### Deploy Services
Navigate to the `user-service` directory and deploy the user service:
   ```bash
   kubectl apply -f user-service.yaml
 ```

Navigate to the `product-service` directory and deploy the product service:
   ```bash
   kubectl apply -f product-service.yaml
 ```

Navigate to the `frontend-service` directory and deploy the user service:
   ```bash
   kubectl apply -f user-service.yaml
 ```

### Access The Application
Get the IP address of your Minikube cluster:
   ```bash
   Minikube ip
 ```
Then, access the frontend using the IP and the corresponding NodePort assigned to the frontend service.


