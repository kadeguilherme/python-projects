from flask import Flask, jsonify, request
from models.ongs import ONGS, ONGSEncoder
from database import db

app = Flask(__name__)
app.config['DEBUG'] = True
app.json_encoder = ONGSEncoder

@app.route('/')
def index():
    return '<h1>Econtre uma ONG</h1><p>Prototipo de API para encontrar ONGs pelo Brasil</p>'


@app.route('/query/ongs', methods=['GET'])
def ongs():
    return jsonify({'ONGS': db})

@app.route('/query/ongs/<int:id>', methods=['GET'])
def list(id):
    for ong in db:
        if ong.new_id == id:
            return jsonify(ong)
    
    return '<h1> ONG não existe</h1>'


@app.route('/post/ong', methods=['POST'])
def creat():
    ong = ONGS(request.json['name'],
                request.json['founder'],
                request.json['sector']
               )
    db.append(ong)
    return jsonify(ong)

@app.route('/delete/ong/<int:id>', methods=['DELETE'])
def delete(id):
    for ong in db:
        if ong.new_id == id:
            db.remove(ong)
            return jsonify({'Usuário excluido': ong})

app.run()