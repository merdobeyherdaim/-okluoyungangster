import sqlite3

def create_table():
    conn = sqlite3.connect('bot_db.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, level INTEGER)''')
    conn.commit()
    conn.close()

def insert_user(id, username):
    conn = sqlite3.connect('bot_db.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (id, username, level) VALUES (?, ?, ?)", (id, username, 1))
    conn.commit()
    conn.close()

def get_user_level(id):
    conn = sqlite3.connect('bot_db.db')
    c = conn.cursor()
    c.execute("SELECT level FROM users WHERE id=?", (id,))
    level = c.fetchone()
    conn.close()
    return level[0] if level else None
