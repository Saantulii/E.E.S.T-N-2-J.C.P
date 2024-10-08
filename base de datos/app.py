from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

# Función para conectar a la base de datos
def get_db_connection():
    conn = sqlite3.connect('escuela.db')
    conn.row_factory = sqlite3.Row
    return conn

# Inicialización de la base de datos
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS forums (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        conn.close()
        if user:
            session['user_id'] = user['id']
            return redirect(url_for('forum'))
    return render_template('login.html')

@app.route('/forum', methods=['GET', 'POST'])
def forum():
    conn = get_db_connection()
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        user_id = session.get('user_id')
        conn.execute('INSERT INTO forums (title, content, user_id) VALUES (?, ?, ?)', (title, content, user_id))
        conn.commit()
        return redirect(url_for('forum'))
    
    posts = conn.execute('SELECT * FROM forums').fetchall()
    conn.close()
    return render_template('forum.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
