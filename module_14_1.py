import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
№ INTEGER PRIMARY KEY,
Имя TEXT NOT NULL,
Почта TEXT NOT NULL,
Возраст INTEGER,
Баланс INTEGER NOT NULL
)
''')

# for i in range(1, 11):
#     cursor.execute('INSERT INTO Users (Имя, Почта, Возраст, Баланс) VALUES (?, ?, ?, ?)',(f'Ded_Serg{i}', f'Ded_Serg{i}@gmail.com', f'{i*10}', '1000'))


# Обновление balance у каждой 2ой записи начиная с 1ой на 500:

# for i in range(1, 11):
#     if i % 2 == 0:
#         pass
#     else:
#         cursor.execute("UPDATE Users SET Баланс = ? WHERE Имя = ?", (500, f"Ded_Serg{i}"))
#
#
# #Удаление каждой 3ей записи в таблице начиная с 1ой:
#
# cursor.execute("DELETE FROM Users WHERE № % 3 = 1")
#
#
# #выбор всех записей
#
cursor.execute("SELECT * FROM Users WHERE Возраст != ?", (60,))
users = cursor.fetchall()
for data in users:
    print(f" Имя: {data[1]} | Почта: {data[2]} | Возраст: {data[3]} | Баланс: {data[4]}")

connection.commit()
connection.close()
