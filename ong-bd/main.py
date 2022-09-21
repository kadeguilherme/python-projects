from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False

db = mysql.connector.connect(
    host ="localhost",
    user="MainUser",
    password="MainPassword",
    database="ONGS",
)

cursor = db.cursor()

sqlselect = ("SELECT * FROM ongs")
sqlinsert = ("INSERT INTO ongs (founder,ongname,sector) VALUES (%s, %s, %s)") 
sqlquery = ("SELECT * FROM ongs WHERE id = {}")
sqlput = ("UPDATE ongs SET founder = '{}' WHERE id = {}")

@app.route("/query/ong", methods=['GET'])
def get():
    cursor.execute(sqlselect)
    ong = cursor.fetchall()
    return ong

@app.route('/post/ong', methods=['POST'])
def post():
    ong = request.json
    data_ong = (ong['founder'], ong['ongname'], ong['sector'])
    cursor.execute(sqlinsert, data_ong)
    db.commit()
    return jsonify("Ong criada",ong)

@app.route('/delete/ong/<int:id>', methods=['DELETE'])
def delete(id):
    cursor.execute(sqlquery.format(id))
    ong = cursor.fetchall()
    db.commit()
    return jsonify("ONG deletada", ong)

@app.route('/resorces/ong/<int:id>', methods=['PUT'])
def put(id):
    ong = request.json
    data_ong = (ong['founder'])
    cursor.execute(sqlput.format(data_ong,id))
    db.commit()
    cursor.execute(sqlquery.format(id))
    ongupdate = cursor.fetchall()

    
    return jsonify("ONG atualizada",ongupdate)
app.run()
