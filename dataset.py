import pandas as pd
import numpy as np
import random

np.random.seed(42)

n_users = 500
n_orders = 5000

users = pd.DataFrame({
    "user_id": range(1, n_users + 1),
    "signup_date": pd.to_datetime("2023-01-01") + pd.to_timedelta(np.random.randint(0, 365, n_users), unit="D"),
    "city": np.random.choice(["São Paulo", "Rio", "Belo Horizonte", "Curitiba"], n_users)
})

orders = pd.DataFrame({
    "order_id": range(1, n_orders + 1),
    "user_id": np.random.randint(1, n_users + 1, n_orders),
    "seller_id": np.random.randint(1, 100, n_orders),
    "order_value": np.random.normal(150, 50, n_orders).round(2),
    "order_date": pd.to_datetime("2024-01-01") + pd.to_timedelta(np.random.randint(0, 180, n_orders), unit="D"),
    "device_id": np.random.randint(1, 800, n_orders)
})



burst_user = random.choice(users["user_id"].tolist())
burst_orders = pd.DataFrame({
    "order_id": range(n_orders+1, n_orders+21),
    "user_id": burst_user,
    "seller_id": np.random.randint(1, 100, 20),
    "order_value": np.random.normal(200, 30, 20).round(2),
    "order_date": pd.to_datetime("2024-06-01"),
    "device_id": np.random.randint(1, 800)
})

orders = pd.concat([orders, burst_orders])

users.to_csv("users.csv", index=False)
orders.to_csv("orders.csv", index=False)