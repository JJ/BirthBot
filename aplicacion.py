from flask import Flask, jsonify,json
from src.birthbot import Birthday

app = Flask(__name__)
    
estadoPorDefecto = {"status": "OK"}

@app.route('/')
def estadoActual():    
    return jsonify(estadoPorDefecto)

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