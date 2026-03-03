WITH burst AS (
    SELECT 
        user_id,
        DATE(order_date) AS order_day,
        COUNT(*) AS orders_per_day
    FROM orders
    GROUP BY user_id, DATE(order_date)
),
stats AS (
    SELECT 
        AVG(orders_per_day) AS mean_orders,
        STDDEV(orders_per_day) AS std_orders
    FROM burst
)

SELECT 
    b.user_id,
    b.order_day,
    b.orders_per_day,
    s.mean_orders,
    s.std_orders
FROM burst b, stats s
WHERE b.orders_per_day > (s.mean_orders + 3 * s.std_orders);