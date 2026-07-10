import sqlite3

conn = sqlite3.connect("SalesDB/sales.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    product_price REAL NOT NULL,
    quantity INTEGER NOT NULL,
    city TEXT NOT NULL,
    order_date TEXT NOT NULL
);

""")

cursor.execute(""" INSERT INTO orders (product_name, product_price, quantity, city, order_date) VALUES 
('Laptop', 1200.00, 2, 'Mumbai', '2022-01-15'),
('Mouse', 25.00, 10, 'Delhi', '2022-01-16'),
('Keyboard', 75.00, 5, 'Bangalore', '2022-01-17'),
('Monitor', 300.00, 3, 'Chennai', '2022-01-18'),
('Headphones', 150.00, 8, 'Kolkata', '2022-01-19');
""")

conn.commit()
conn.close()


