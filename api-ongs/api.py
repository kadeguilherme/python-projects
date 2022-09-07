from flask import Flask, jsonify
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







app.run()