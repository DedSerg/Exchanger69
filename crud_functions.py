import sqlite3
from distutils.util import execute

connection = sqlite3.connect("prod_base.db")
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    № INTEGER PRIMARY KEY,
    Название TEXT NOT NULL,
    Описание TEXT ,
    Цена INTEGER NOT NULL,
    Ед TEXT NOT NULL)
   ''')

    cursor.execute('''
    DELETE FROM Products
    ''')


initiate_db()

for i in range(1, 5):
    cursor.execute('INSERT INTO Products (Название, Описание, Цена, Ед) VALUES (?, ?, ?, ?)',
                   (f'Product {i}', f'Описание {i}', i * 100, 'кг'))


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()


connection.commit()
# connection.close()
