# 📊 Ecommerce Fraud Detection Pipeline (ETL & Orchestration)

This repository demonstrates a complete data engineering lifecycle for fraud prevention. It goes beyond simple analysis, implementing a robust **ETL pipeline** orchestrated by **Apache Airflow** to identify anomalous patterns in a simulated e-commerce environment.

---

## 📁 Project Architecture

The project is structured into two main modules to reflect real-world production environments:

- **`fraud-analysis-lab/`**: Initial exploratory data analysis (PoC), where statistical thresholds and fraud rules were defined.
- **`fraud-automation-engine/`**: The production-ready version featuring:
    - **Extraction:** Data retrieval from a PostgreSQL transactional database.
    - **Transformation:** Statistical anomaly detection using Python (Pandas) and SQL.
    - **Loading:** Persistent alert generation in dedicated database tables and audit logs.

### Key Fraud Patterns Detected:
- **Burst Transactions:** Abnormal spikes in purchases by the same user within a single day.
- **Shared Device Usage:** Multiple users associated with the same device beyond a statistical threshold ($Mean + 3 \times StdDev$).

---

## 🛠️ Tools & Technologies

- **Language:** Python (Pandas, SQLAlchemy)
- **Database:** PostgreSQL (Relational storage & Analytical queries)
- **Orchestration:** Apache Airflow (DAGs, PythonOperators, Scheduling)
- **Infrastructure:** Docker & Docker Compose (Containerization of the entire stack)

---

## ⚙️ Automation & Pipeline Features

- **Hourly Orchestration:** The pipeline is scheduled to run every hour, ensuring near real-time risk monitoring.
- **Scalable Architecture:** Use of Docker volumes to separate responsibilities between source code (`src/`), infrastructure (`setup/`), and raw data (`data/`).
- **Statistical Thresholding:** Dynamic detection based on standard deviation, avoiding hard-coded limits and adapting to data behavior.
- **Dual-Alert System:** Simultaneous output to PostgreSQL `fraud_alerts` table for system integration and `.log` files for manual auditing.

---

## 🎯 Skills Demonstrated

- **Data Engineering:** Building ETL pipelines and managing database connections.
- **DevOps/Infra:** Containerization with Docker and environment orchestration.
- **Statistical Analysis:** Applying $Z$-score logic for outlier detection.
- **Analytical Reasoning:** Mapping business fraud rules into automated technical solutions.