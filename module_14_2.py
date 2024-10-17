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
# удаление пользователя id=6
# cursor.execute("DELETE FROM Users WHERE № = ?", (6,))
# подсчёт общего кол-ва записей
cursor.execute("SELECT COUNT(*) FROM Users")
tot_1 = cursor.fetchone()[0]
print(tot_1)
# сумма всех балансов
cursor.execute("SELECT SUM(Баланс) FROM Users")
tot_2 = cursor.fetchone()[0]
print(tot_2)
# средний баланс
# a.
print(tot_2/tot_1)
# b.
cursor.execute("SELECT AVG(Баланс) FROM Users")
avg_bal = cursor.fetchone()[0]
print(avg_bal)








connection.commit()
connection.close()
