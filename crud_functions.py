import sqlite3
from distutils.util import execute

connection = sqlite3.connect("prod_base.db")
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    № INTEGER PRIMARY KEY,
    Имя TEXT NOT NULL ,
    Почта TEXT NOT NULL ,
    Возраст INTEGER NOT NULL,
    Баланс INTEGER NOT NULL)
    ''')
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
def add_user(username, email, age):
    cursor.execute('INSERT INTO Users (Имя, Почта, Возраст, Баланс) VALUES (?, ?, ?, ?)' ,
                   (username, email, age, 1000)
                   )
    connection.commit()

def is_included(username):
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    for user in users:
        if user[1] == username:
            return True
    return False

def get_all_products():
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()



connection.commit()
# connection.close()
