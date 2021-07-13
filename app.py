from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return "Hola, este es un ejemplo."

@app.route("/nuevapagina")
def index():
    return "Hola, este es un ejemplo."