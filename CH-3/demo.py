import sqlite3
import sqlite3

conn = sqlite3.connect("SalesDB/sales.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM orders")

print(cursor.fetchall())  

conn.close()