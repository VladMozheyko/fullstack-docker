from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="db",
        user="root",
        password="password",
        database="testdb"
    )

@app.route("/users")
def users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM users;")
    result = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return jsonify(result)

@app.route("/")
def home():
    return "API работает!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

