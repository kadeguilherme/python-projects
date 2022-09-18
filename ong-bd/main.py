from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False

db = mysql.connector.connect(
    host ="localhost",
    user="MainUser",
    password = "MainPassword",
    database="ONGS",
)

cursor = db.cursor()
cursor.execute('SELECT * FROM ongs')


@app.route("/query/ong", methods=['GET'])
def get():
    ong = cursor.fetchall()
    return ong

app.run()