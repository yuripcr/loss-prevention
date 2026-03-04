![Python](https://img.shields.io/badge/Python-3.11-blue)
![Docker](https://img.shields.io/badge/Docker-Ready-lightgrey)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)
![Airflow](https://img.shields.io/badge/Airflow-2.10-blue)

# 📊 Ecommerce Fraud Detection Pipeline 

Complete data engineering lifecycle for fraud prevention, featuring a robust ETL pipeline orchestrated with Apache Airflow to detect anomalous patterns in a simulated e-commerce environment.

---

## 📁 Project Architecture

The project is structured into two main modules to reflect real-world production environments:

- **`fraud-analysis-lab/`**: Initial exploratory data analysis where fraud rules and behavioral thresholds were defined.
- **`fraud-automation-engine/`**: The production-ready version featuring:
    - **Extraction:** Automated data retrieval from a PostgreSQL transactional database.
    - **Transformation:** Behavioral anomaly detection using Python (Pandas) and SQL.
    - **Loading:** Persistent alert generation in dedicated database tables and audit logs.

### Key Fraud Patterns Detected:
- **Burst Transactions:** : Detection of abnormal purchase spikes by the same user within a single day.
- **Shared Device Usage:** Detection of multiple accounts linked to a single device based on behavioral outliers.

---

## 🛠️ Tools & Technologies

- **Language:** Python (Pandas, SQLAlchemy)
- **Database:** PostgreSQL (Relational storage & Analytical queries)
- **Orchestration:** Apache Airflow (DAGs, PythonOperators, Scheduling)
- **Infrastructure:** Docker & Docker Compose (Containerization of the entire stack)

---

## ⚙️ Automation & Pipeline Features

- **Hourly Orchestration:** The pipeline is scheduled to run every hour, ensuring frequent and automated risk monitoring.
- **Dynamic Thresholding:** Detection logic that adapts to data behavior to identify outliers instead of using fixed/hard-coded limits.
- **Dual-Alert System:** Simultaneous output to a PostgreSQL `fraud_alerts` table for system integration and `.log` files for manual auditing.

---

## 🎯 Skills Demonstrated

- **Data Engineering:** Building end-to-end ETL pipelines and managing database connections.
- **DevOps/Infra:** Containerization with Docker and environment orchestration for data workflows.
- **Fraud Detection:** Mapping e-commerce business rules into automated technical solutions.
- **Problem Solving:** Implementing logic to transform raw transactional data into actionable security flags.