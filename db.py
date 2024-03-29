import sqlite3

db_name ='db.sqlite'

conn = None
cursor=None
def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()

def do(query):
    cursor.execute(query)
    conn.commit()

def create_tables():
    open()
    do('''CREATE TABLE IF NOT EXISTS products (prod_id INTEGER PRIMARY KEY,
       prod_name VARCHAR,
       prod_price FLOAT,
       prod_img VARCHAR
       )''')
    close()

def drop_table():
    open()
    do('DROP TABLE IF EXISTS products')
    close()

def show_tables():
    open()
    cursor.execute('''SELECT * FROM products''')
    print(cursor.fetchall())
    close()

def get_all_products():
    open()
    cursor.execute('''SELECT * FROM products''')
    
    return cursor.fetchall()
    close()
def get_prod_by_id(id):
    open()
    cursor.execute('''SELECT prod_id, prod_name, prod_price FROM products WHERE prod_id=(?)''',[id])
    return cursor.fetchone()

def add_products(prod_name, prod_price, prod_img):
    open()
    cursor.execute('''INSERT INTO products 
                   (prod_name, prod_price, prod_img) 
                   VALUES (?, ?, ? )''', [prod_name, prod_price, prod_img])
    conn.commit()
    close()

#create_tables()
#show_tables()
#
#add_products('Banana',2.99,'https://ovocheva-poshta.com.ua/images/virtuemart/product/banan8.jpg')
#show_tables()
