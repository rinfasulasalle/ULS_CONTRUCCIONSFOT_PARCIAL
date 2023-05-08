from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 

from backend.models.mysql_curso_model import cursoModel
model = cursoModel()

curso_blueprint = Blueprint('curso_blueprint', __name__)

@curso_blueprint.route('/curso', methods=['PUT'])
@cross_origin()
def create_curso():
    content = model.create_curso(request.json['nombre_curso'])    
    return jsonify(content)

@curso_blueprint.route('/curso', methods=['PATCH'])
@cross_origin()
def update_curso():
    content = model.update_curso(request.json['id_curso'], request.json['nombre_curso'])     
    return jsonify(content)

@curso_blueprint.route('/curso', methods=['DELETE'])
@cross_origin()
def delete_curso():
    return jsonify(model.delete_curso(int(request.json['id_curso'])))

@curso_blueprint.route('/curso', methods=['POST'])
@cross_origin()
def curso():
    return jsonify(model.get_curso(int(request.json['id_curso'])))

@curso_blueprint.route('/cursos', methods=['POST'])
@cross_origin()
def cursos():
    return jsonify(model.get_cursos())