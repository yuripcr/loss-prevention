import pandas as pd

orders = pd.read_csv("../orders.csv")

# dispositivo compartilhado
device_check = (
    orders.groupby("device_id")["user_id"]
    .nunique()
    .reset_index(name="unique_users")
)

mean_users = device_check["unique_users"].mean()
std_users = device_check["unique_users"].std()

threshold_device = mean_users + 3 * std_users

shared_devices = device_check[device_check["unique_users"] > threshold_device]

print("\nDevices compartilhados por muitos usuários:")
print(shared_devices)

# compras por dia
orders["order_date"] = pd.to_datetime(orders["order_date"])
orders["order_day"] = orders["order_date"].dt.date

burst = (
    orders.groupby(["user_id", "order_day"])
    .size()
    .reset_index(name="orders_per_day")
)

mean_orders = burst["orders_per_day"].mean()
std_orders = burst["orders_per_day"].std()

threshold = mean_orders + 3 * std_orders

suspicious_burst = burst[burst["orders_per_day"] > threshold]

print("\nUsuários com pico de compras no mesmo dia:")
print(suspicious_burst)

print("\nmean:", mean_orders)
print("std:", std_orders)
print("threshold:", threshold)