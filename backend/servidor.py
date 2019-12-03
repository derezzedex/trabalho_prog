from flask import Flask, json, jsonify, request
from classes import *
from playhouse.shortcuts import model_to_dict
import sys

app = Flask(__name__)

def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)

@app.route('/listar/<classe>')
def listar(classe):
    try:
        classe = str_to_class(classe)
    except AttributeError as erro:
        response = jsonify({"resultado": "Erro", "detalhes": "Classe não existe!"})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    lista = [model_to_dict(linha, manytomany=True, recurse=True) for linha in classe.select()]
    response = jsonify({"resultado": "Ok", "lista": lista})

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

app.run(debug=True, port=4999)
