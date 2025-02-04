from main import app
from flask import render_template
from dataColector import getSheetsData

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/simulacao")
def simulacao():
    locacoes = [{
        'locataria': str,
        'link':str,
        'salas':int,
        'bairro':str,
        'valor':float,
        'cod':str
    }]
    data = getSheetsData()
    print(data[1][0])
    return render_template("simulacao.html", )