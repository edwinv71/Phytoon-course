import sqlite3
# import os

# 1. create a connection object
conn = sqlite3.connect("my_database.db")
# 2. declare context manager
with conn:
    c = conn.cursor()
    c.execute(
        """CREATE TABLE products  (
            prodId text,
            description text,
            price float
            )"""
    )
    c.execute("INSERT INTO products VALUES (:prodId, :description, :price)", 
                {'prodId': '111', 'description': 'Earl grey', 'price': 1.99})

    c.execute("INSERT INTO products VALUES (:prodId, :description, :price)", 
                {'prodId': '222', 'description': 'Americano', 'price': 2.50})
    
    c.execute("INSERT INTO products VALUES (:prodId, :description, :price)", 
                {'prodId': '333', 'description': 'Capuccino', 'price': 3.00})
    
    c.execute("INSERT INTO products VALUES (:prodId, :description, :price)", 
                {'prodId': '444', 'description': 'Caffe Late', 'price': 3.50})
    
    c.execute("INSERT INTO products VALUES (:prodId, :description, :price)", 
                {'prodId': '555', 'description': 'Flat white', 'price': 3.50})
    
    c.execute("INSERT INTO products VALUES (:prodId, :description, :price)", 
                {'prodId': '666', 'description': 'Hot chocolate', 'price': 3.65})
            
