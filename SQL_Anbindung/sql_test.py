import sqlite3

conn = sqlite3.connect("test1.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS kunden (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    age INTEGER
)
""")
conn.commit()  # Änderungen speichern

cursor.execute("INSERT INTO kunden (name, email, age) VALUES (?,?, ?)",
    ("Max Mustermann", "max@mustermann.com", 30))

conn.commit()