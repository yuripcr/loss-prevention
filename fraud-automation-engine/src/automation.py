import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime

engine = create_engine(
    "postgresql+psycopg2://airflow:airflow@postgres:5432/loss_prev"
)

def run_fraud_detection():

    print("Iniciando análise...")

    orders = pd.read_sql("SELECT * FROM orders", engine)

    # Device compartilhado

    device_check = (
        orders.groupby("device_id")["user_id"]
        .nunique()
        .reset_index(name="unique_users")
    )

    threshold_device = (
        device_check["unique_users"].mean()
        + 3 * device_check["unique_users"].std()
    )

    shared_devices = device_check[
        device_check["unique_users"] > threshold_device
    ]

    # Burst de compras

    orders["order_date"] = pd.to_datetime(orders["order_date"])
    orders["order_day"] = orders["order_date"].dt.date

    burst = (
        orders.groupby(["user_id", "order_day"])
        .size()
        .reset_index(name="orders_per_day")
    )

    threshold_burst = (
        burst["orders_per_day"].mean()
        + 3 * burst["orders_per_day"].std()
    )

    suspicious_burst = burst[
        burst["orders_per_day"] > threshold_burst
    ]

    print("Devices suspeitos:", len(shared_devices))
    print("Usuários suspeitos:", len(suspicious_burst))

    generate_log(shared_devices, suspicious_burst)
    save_alerts(shared_devices, suspicious_burst)

def generate_log(shared_devices, suspicious_burst):
    if not shared_devices.empty or not suspicious_burst.empty:
        # Coloque o caminho completo apontando para a pasta dags compartilhada
        caminho_arquivo = "/opt/airflow/dags/fraud_alert.log"
        
        with open(caminho_arquivo, "a", encoding="utf-8") as f:
            f.write(f"\n=== ALERTA {datetime.now()} ===\n")
            f.write("Dispositivos suspeitos:\n")
            f.write(shared_devices.to_string())
            f.write("\n\nUsuários com pico de compras:\n")
            f.write(suspicious_burst.to_string())
            f.write("\n=========================\n")

def save_alerts(shared_devices, suspicious_burst):

    with engine.begin() as conn:

        for _, row in shared_devices.iterrows():
            conn.execute(
                text("""
                    INSERT INTO fraud_alerts (alert_type, reference_id)
                    VALUES (:type, :ref)
                """),
                {"type": "shared_device", "ref": int(row["device_id"])}
            )

        for _, row in suspicious_burst.iterrows():
            conn.execute(
                text("""
                    INSERT INTO fraud_alerts (alert_type, reference_id)
                    VALUES (:type, :ref)
                """),
                {"type": "burst_user", "ref": int(row["user_id"])}
            )

if __name__ == "__main__":
    run_fraud_detection()