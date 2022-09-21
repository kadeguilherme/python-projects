import mysql.connector
from flask import Flask, jsonify, request

db = mysql.connector.connect(
    host ="localhost",
    user="MainUser",
    password = "MainPassword",
    database="Pycodebr",
)


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False
cursor = db.cursor()


@app.route("/query/ongs", methods=['GET'])
def ongs():
    
    cursor.execute('SELECT * FROM carros')
    ong = cursor.fetchall()
    return ong


@app.route("/resorces/ong", methods=['POST'])
def post():
    carro = request.json
    # sql = f"INSERT INTO carros (marca, modelo, ano) VALUES ('{marca}', '{modelo}' , '{ano}')"
    sql = ("INSERT INTO carros (marca, modelo, ano) VALUES (%s,%s , %s)")
    data_carro = (carro['marca'],carro['modelo'],carro['ano'])
    cursor.execute(sql, data_carro)
    db.commit()
    return jsonify(carro)


@app.route("/delete/ong/<int:id>", methods=['DELETE'])
def delete(id):
    
    select = db.cursor()
    where = ("SELECT * FROM carros WHERE id = {}").format(id)
    select.execute(where)
    carro = select.fetchall()

    sql = ("DELETE FROM carros WHERE id = {}").format(id)
    select.execute(sql)
    db.commit()
    print(carro)

    return jsonify(carro)
    


app.run()