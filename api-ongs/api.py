from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return '<h1>Econtre uma ONG</h1><p>Prototipo de API para encontrar ONGs pelo Brasil</p>'

app.run()