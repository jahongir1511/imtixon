import sqlite3

# Ma'lumotlar bazasiga ulanish
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Jadval yaratish
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

print("Jadval yaratildi!")

# Ma'lumot qo'shish
cursor.execute('''
INSERT INTO users (name, age) VALUES (?, ?)
''', ("Ali", 25))

# O'zgarishlarni saqlash
conn.commit()

print("Ma'lumot qo'shildi!")

# Ma'lumotlarni o'qish
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

print("Foydalanuvchilar:")
for row in rows:
    print(row)

# Ma'lumotni yangilash
cursor.execute('''
UPDATE users SET age = ? WHERE name = ?
''', (26, "Ali"))

# O'zgarishlarni saqlash
conn.commit()

print("Ma'lumot yangilandi!")

# Ma'lumotlarni qayta o'qish
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

print("Yangilangan foydalanuvchilar:")
for row in rows:
    print(row)

# Ma'lumotni o'chirish
cursor.execute('''
DELETE FROM users WHERE name = ?
''', ("Ali",))

# O'zgarishlarni saqlash
conn.commit()

print("Ma'lumot o'chirildi!")

# Kursorni yopish
cursor.close()

# Ulanishni yopish
conn.close()

print("Ma'lumotlar bazasi ulanishi yopildi!")
