# 🚀 Deploying and Managing Microservices in a Cloud-Native Environment

This project demonstrates how to deploy and manage a microservices-based application using Kubernetes. It includes containerized services, Kubernetes deployments, autoscaling, service discovery, and persistent storage.

---

## 📌 Project Objective

- Set up and configure a Kubernetes cluster (Minikube used for local setup)
- Containerize and deploy microservices (User, Product, Order services)
- Manage Kubernetes Deployments, Services, Autoscaling, and Persistent Volumes

---

## 📂 Microservices Overview

The following microservices are deployed in the Kubernetes cluster:

| Service         | Port | Description                        |
|------------------|------|------------------------------------|
| user-service     | 5000 | Handles user-related operations    |
| product-service  | 5001 | Manages product data               |
| order-service    | 5002 | Stores orders using persistent volume |

Each service includes:
- A Dockerfile
- Python Flask app (`app.py`)
- Kubernetes Deployment & Service YAML files

---

## ⚙️ Kubernetes Components

### ✅ Deployments
Located in `deployments/` folder.

- Defines container image, replicas, ports, etc.
- Example: `user-deployment.yaml`, `product-deployment.yaml`, `order-deployment.yaml`

### ✅ Services
Located in `services/` folder.

- Exposes microservices internally (ClusterIP) or externally (NodePort)
- Example: `user-service.yaml`, `product-service.yaml`, `order-service.yaml`

### ✅ Autoscaling (HPA)
Located in `hpa/` folder.

- Configured for `product-service` based on CPU usage
- File: `product-hpa.yaml`

### ✅ Storage (Persistent Volume)
Located in `storage/` folder.

- Used by `order-service` to persist data even if pod restarts
- Files: `pv.yaml`, `pvc.yaml`

---

## 🐳 Docker Image Information

| Service         | Docker Image                            |
|------------------|-----------------------------------------|
| user-service     | `achal0356/user-service:latest`         |
| product-service  | `achal0356/product-service:latest`      |
| order-service    | `achal0356/order-service:latest`        |

---

## 🛠 Prerequisites

- [Docker](https://www.docker.com/)
- [Minikube](https://minikube.sigs.k8s.io/docs/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- (Optional) Docker Hub account for pushing images

---

## 🚀 How to Run This Project

### 1. Start Minikube
minikube start

Apply Kubernetes Manifests
	kubectl apply -f storage/
	kubectl apply -f deployments/
	kubectl apply -f services/
	kubectl apply -f hpa/

Access Services
	Get Minikube IP and open the service in browser:
		minikube service user-service
		minikube service product-service
		minikube service order-service

## 📈 Horizontal Pod Autoscaler (HPA)

Check autoscaling behavior:
	kubectl get hpa

Generate load for product-service:
	while true; do curl http://<minikube-ip>:30002/; done

## 💾 Persistent Volume Test
Open order-service endpoint.
It writes to /data/order.txt inside the persistent volume.
Delete pod and re-check — data will still be available.

## 🧰 Tools Used
Docker & Docker Hub
Python (Flask)
Kubernetes (Minikube)
kubectl
Horizontal Pod Autoscaler
Persistent Volume & Claim

