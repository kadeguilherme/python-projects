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

sqlinsert = ("INSERT INTO ongs (founder,ongname,sector) VALUES (%s, %s, %s)") 

@app.route("/query/ong", methods=['GET'])
def get():
    cursor.execute('SELECT * FROM ongs')
    ong = cursor.fetchall()
    return ong

@app.route('/post/ong', methods=['POST'])
def post():
    ong = request.json
    data_ong = (ong['founder'], ong['ongname'], ong['sector'])
    cursor.execute(sqlinsert, data_ong)
    db.commit()
    return jsonify("Ong criada",ong)


app.run()