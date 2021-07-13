from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return "Hola, este es un ejemplo, texto modificado."

@app.route("/nuevapagina")
def index():
    return "Hola, este es un ejemplo en otra página."


if __name__ == "__main__":
    app.run()