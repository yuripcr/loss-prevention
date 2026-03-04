import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg2://airflow:airflow@postgres:5432/loss_prev"
)

def setup_database():
    print("Lendo os arquivos CSV...")
    orders_df = pd.read_csv("data/orders.csv")
    users_df = pd.read_csv("data/users.csv")

    print("Enviando dados para o PostgreSQL...")
    # O comando to_sql cria a tabela automaticamente e insere os dados!
    orders_df.to_sql("orders", engine, if_exists="replace", index=False)
    users_df.to_sql("users", engine, if_exists="replace", index=False)
    print("Tabelas 'orders' e 'users' criadas com sucesso!")

    print("Criando tabela 'fraud_alerts' para salvar os resultados...")
    with engine.begin() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS fraud_alerts (
                id SERIAL PRIMARY KEY,
                alert_type VARCHAR(50),
                reference_id INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """))
    print("Tabela 'fraud_alerts' pronta!")

if __name__ == "__main__":
    setup_database()