from flask import Flask, jsonify
from database import db

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return '<h1>Econtre uma ONG</h1><p>Prototipo de API para encontrar ONGs pelo Brasil</p>'


@app.route('/query/ongs', methods=['GET'])
def ongs():
    return jsonify({'ONGS': db})




app.run()