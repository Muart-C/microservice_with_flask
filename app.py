from flask import Flask, g
import sqlite3

#configuration
DATABASE = 'flasktdd.db'
SECRET_KEY = 'my-secret_key'
DEBUG = True
USERNAME = 'admin'
PASSWORD = 'password'

app = Flask(__name__)
app.config.from_object(__name__)


def connect_database():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def create_database():
    with app.app_context():
        db = db_connection()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def db_connection():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_database()
    return g.sqlite_db

@app.teardown_appcontext
def close_connection(error):
    if hasattr(g, "sqlite_db"):
        g.sqlite_db.close()


@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == "__main__":
    create_database()
    app.run()