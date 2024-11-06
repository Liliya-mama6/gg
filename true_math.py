import sqlite3

contact = sqlite3.connect('dt.db')
cursor = contact.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS User(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
cursor.execute('''
CREATE INDEX IF NOT EXISTS idx_email ON User(email)
''')

for i in range(10):
   cursor.execute('INSERT INTO User(username, email, age, balance) VALUES (?, ?, ?, ?)',
                 (f'user{i+1}', f'example{i+1}@gmail.com', f'{10*(i+1)}', f'{1000}'))

for i in range(1, 11, 2):
    cursor.execute('UPDATE User SET balance = ? WHERE age = ?', (500, i*10))

for i in range(1, 11, 3):
    cursor.execute('DELETE FROM User WHERE age = ?', (i*10, ))

cursor.execute('SELECT username, email, age, balance FROM User WHERE age != ?', (60, ))
users=cursor.fetchall()
for i in users:
    print(*i)

contact.commit()
contact.close()
