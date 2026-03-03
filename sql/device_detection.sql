
WITH device_check AS (
    SELECT
        device_id,
        COUNT(DISTINCT user_id) AS unique_users
    FROM orders
    GROUP BY device_id
),
stats AS (
    SELECT
        AVG(unique_users) AS mean_users,
        STDDEV(unique_users) AS std_users
    FROM device_check
)

SELECT 
    d.device_id,
    d.unique_users,
    s.mean_users,
    s.std_users,
    (s.mean_users + 3 * s.std_users) AS threshold
FROM device_check d, stats s
WHERE d.unique_users > (s.mean_users + 3 * s.std_users);