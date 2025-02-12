# airflow-exercises

This project uses Apache Airflow to manage workflows. Below are the steps to set up and run the project on your local machine using Docker.

---

## Prerequisites

Before you begin, ensure you have the following installed:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)

---

## Setup Instructions

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone <repository-url>
cd <repository-folder>
```

### Step 2: Initialize Airflow Database
Run the following command to initialize the Airflow database (PostgreSQL):
``` bash 
docker-compose up airflow-init
```
This will set up the necessary database tables for Airflow.

### Step 3: Start Airflow Services
Start the Airflow services in detached mode:

``` bash 
docker-compose up -d
```
This will start Airflow along with its dependencies (PostgreSQL, Redis, etc.).

### Step 4: Access Airflow Web UI
Once the services are running, open your browser and navigate to:

``` bash 
http://localhost:8080/
```
The default credentials are:

Username: airflow
Password: airflow

### Step 5: Configure PostgreSQL Connection in Airflow
To connect Airflow to the PostgreSQL database, follow these steps:

1 - Go to Admin > Connections in the Airflow UI.
2 - Click on Add a new record.
Fill in the connection details:
    - Connection Id: postgres (must match the connection ID used in your DAGs)
    - Connection Type: Postgres
    - Host: postgres
    - Schema: airflow
    - Login: airflow
    - Password: airflow
    - Port: 5432

If you are using an external PostgreSQL instance, replace the connection details with your own.

### Step 6: Run Your DAGs
Once the connection is configured, you can trigger your DAGs from the Airflow UI. Ensure everything is running successfully.

### Troubleshooting
If you encounter issues, check the logs for the specific service using:

``` bash 
docker-compose logs <service-name>
```

### Stopping the Services

To stop the running services, use:

``` bash 
docker-compose down
```



