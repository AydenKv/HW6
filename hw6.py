import sqlite3

db = sqlite3.connect('game.db')

cursor_ = db.cursor()

cursor_.execute('''CREATE TABLE IF NOT EXISTS users(
name TEXT, 
age INTEGER,
password TEXT
)''')

cursor_.execute('''INSERT INTO users VALUES('Aydin', 15, 'qwerty')''')
cursor_.execute('''INSERT INTO users VALUES('James', 45, '12345')''')


db.commit()
db.close()