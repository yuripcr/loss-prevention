from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

sys.path.append("/opt/airflow")

from src.automation import run_fraud_detection

default_args = {
    "owner": "yuri",
    "start_date": datetime(2024, 1, 1),
}

with DAG(
    dag_id="fraud_monitoring_pipeline",
    default_args=default_args,
    schedule="@hourly",
    catchup=False,
) as dag:

    run_analysis = PythonOperator(
        task_id="run_fraud_detection",
        python_callable=run_fraud_detection
    )

    run_analysis