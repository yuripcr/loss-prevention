CREATE TABLE users (
    user_id INT PRIMARY KEY,
    signup_date DATE,
    city VARCHAR(50)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    seller_id INT,
    order_value NUMERIC(10,2),
    order_date TIMESTAMP,
    device_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
