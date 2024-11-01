import sqlite3

m = 100

with sqlite3.connect('my_database.db') as conn:
    c = conn.cursor()
    print(type(conn))#<class 'sqlite3.Connection'>

    c.execute("SELECT * FROM products")
    all_items = c.fetchall()
    print(type(all_items))#<class 'list'>

    print("All items:")
    for item in all_items:
        print(item)
    print("*" * m)

    # different queries:
    c.execute("SELECT * FROM products WHERE price > :price", {'price': 3.00})
    price_over_3 = c.fetchall()
    print("All items over £3")
    for item in price_over_3:
        print(item)
    print("*" * m)

    # updating
    c.execute("""UPDATE products SET price = :price 
              WHERE prodId = :prodId""",
              {'prodId': '111', 'price': 10.50})
    c.execute("""DELETE FROM products
              WHERE description = :description""",
              {'description': 'Flat white'})
    
    c.execute("SELECT * FROM products")
    
    edited_items = c.fetchall()
    print("After updating earl Grey and deleting flat white")
    for item in edited_items:
        print(item)
    print("*" * m)
    
