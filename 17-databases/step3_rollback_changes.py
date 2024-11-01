import sqlite3

m = 100

with sqlite3.connect('my_database.db') as conn:
    c = conn.cursor()

    c.execute("SELECT * FROM products")
    all_items = c.fetchall()

    print("All items:")
    for item in all_items:
        print(item)
    print("*" * m)

    # updating
    c.execute("""UPDATE products SET price = :price 
              WHERE prodId = :prodId""",
              {'prodId': '111', 'price': 1.99})
    c.execute("""INSERT INTO products VALUES
              (:prodId, :description, :price)""",
              {'prodId': '555', 'description': 'Flat white', 'price': 3.50})
    
    c.execute("SELECT * FROM products")
    
    edited_items = c.fetchall()
    print("After rolling back earl Grey and flat white updates")
    for item in edited_items:
        print(item)
    print("*" * m)
    
