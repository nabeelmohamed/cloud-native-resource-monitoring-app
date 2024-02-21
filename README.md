# Cloud Native Resource Monitoring Python App on Kubernetes

This project demonstrates how to create a cloud-native resource monitoring application using Python, Flask, Docker, AWS EKS, and Kubernetes. The application monitors system metrics like CPU and memory usage and displays them in a user-friendly web interface.

## Prerequisites

- AWS Account
- Programmatic access and AWS configured with CLI
- Python3 Installed
- Docker and Kubectl installed
- Code editor (Vscode)

## Getting Started

### Part 1: Running the Flask Application Locally

1. Clone the repository: `git clone <repository_url>`
2. Install dependencies: `pip3 install -r requirements.txt`
3. Run the application: `python3 app.py`

### Part 2: Dockerizing the Flask Application

1. Create a Dockerfile
2. Build the Docker image: `docker build -t <image_name> .`
3. Run the Docker container: `docker run -p 5000:5000 <image_name>`

### Part 3: Pushing the Docker Image to ECR

1. Create an ECR repository using Python
2. Push the Docker image to ECR: `docker push <ecr_repo_uri>:<tag>`

### Part 4: Creating an EKS Cluster and Deploying the App Using Python

1. Create an EKS cluster and add a node group
2. Create a node group in the EKS cluster
3. Create a deployment and service (make sure to edit the name of the image on line 25 with your image URI)

Once you run `python3 eks.py`, the deployment and service will be created. You can check by running the following commands:

- `kubectl get deployment -n default`
- `kubectl get service -n default`
- `kubectl get pods -n default`

Once your pod is up and running, run the port-forward to expose the service: `kubectl port-forward service/<service_name> 5000:5000`

## Acknowledgements

This project was inspired by a YouTube tutorial. I forked the original repository and added my own modifications to enhance the functionality of the application.
