from flask import Flask, jsonify,json
from src.birthbot import Birthday

app = Flask(__name__)

#Devuelvo siempre status.json 

@app.route('/')
def estadoActual():  
    cumple = Birthday()
    estado = cumple.status()

    if estado:
        with open('status.json') as j:
            respuesta = json.load(j)

    return jsonify(respuesta) 

@app.route('/status')
def status():
    cumple = Birthday()
    estado = cumple.status()

    if estado:
        with open('status.json') as j:
            respuesta = json.load(j)

    return jsonify(respuesta)            

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)