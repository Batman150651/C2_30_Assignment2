# StudentProject: Multi-App Django Project with Docker & Jenkins

## **Project Overview**
This project is a **multi-app Django web application** that has been containerized using **Docker** and automated with **Jenkins**. It includes:
- A Django project (`StudentProject`) with two apps (`app1` and `app2`).
- Static pages rendered using Django templates.
- A **Dockerfile** for containerization.
- A **Jenkins pipeline** for CI/CD.
- Automated deployment to **Docker Hub**.

---

## **Project Structure**
```
StudentProject/
│── StudentProject/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│── app1/
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│       ├── home.html
│── app2/
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│       ├── sample.html
│── Dockerfile
│── Jenkinsfile
│── requirements.txt
│── manage.py
│── README.md
```

---

## **How to Run the Project Locally**
### **1️⃣ Install Dependencies**
Ensure you have **Python** and **Docker** installed. Then, install Django:
```bash
pip install django
```

### **2️⃣ Run Django Locally**
```bash
python manage.py runserver
```
Access the app at **http://127.0.0.1:8000/**.

---

## **Dockerization**
### **1️⃣ Build the Docker Image**
```bash
docker build -t studentproject .
```

### **2️⃣ Run the Docker Container**
```bash
docker run -p 8000:8000 studentproject
```
Visit **http://localhost:8000/** to see the running application.

---

## **Jenkins CI/CD Pipeline**
### **1️⃣ Setup Jenkins Pipeline**
1. Go to **Jenkins Dashboard** → **New Item** → **Pipeline** → **OK**.
2. In **Pipeline Definition**, select **Pipeline script from SCM**.
3. Set **Script Path** to `Jenkinsfile`.
4. Save and **Build Now**.

### **2️⃣ Jenkinsfile (CI/CD Pipeline)**
```groovy
pipeline {
    agent any
    environment {
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub-creds')
        DOCKER_IMAGE = 'your-dockerhub-username/studentproject'
    }
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/your-username/your-repo.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }
        stage('Login to Docker Hub') {
            steps {
                sh 'echo $DOCKER_HUB_CREDENTIALS_PSW | docker login -u $DOCKER_HUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('Push to Docker Hub') {
            steps {
                sh 'docker push $DOCKER_IMAGE'
            }
        }
    }
}
```

---

## **Docker Hub Deployment**
### **1️⃣ Push Docker Image to Docker Hub**
```bash
docker login
docker tag studentproject your-dockerhub-username/studentproject:latest
docker push your-dockerhub-username/studentproject:latest
```

### **2️⃣ Verify on Docker Hub**
Visit **https://hub.docker.com/repositories** to see your uploaded image.

---

## **Submission Details**
- **GitHub Repository**: [GitHub Repo Link](#)
- **Docker Hub Repository**: [Docker Hub Link](#)

📌 **Deadline: March 24, 2025** (Ensure entries are logged in the `assignment2_results` sheet).


