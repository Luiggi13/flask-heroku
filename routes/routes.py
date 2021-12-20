from flask import Flask, jsonify, request, send_from_directory
from flask import Blueprint
from os import abort, getcwd
from handlers.compress import *
from models.model import carList, carNotFound

API_PREFIX = '/api/v1'
PATH_FILE = "%s/Customs/Cars/" % (getcwd())
DOWNLOAD_PATH = "%s/skins/" % (getcwd())

cars_api = Blueprint('cars_api', __name__)
apifile_api = Blueprint('apifile', __name__)
files_api = Blueprint('files_api', __name__)
health_api = Blueprint('health_api', __name__)

#CARS ENDPOINT
@cars_api.route(API_PREFIX +'/cars/',methods=['GET'])
def listarCarsCompleted():    
    return jsonify(carList())

@cars_api.route(API_PREFIX +'/cars/<idCar>',methods=['GET'])
def listarCars(idCar):    
    for element in carList():
        if (str(element['id_car']) == str(idCar)):
            return jsonify(element)
        else:
            return jsonify(carNotFound())
    return jsonify(carList())
#FILES ENDPOINTS
@apifile_api.route(API_PREFIX +'/clear_all/',methods=['DELETE'])
def deleteFiles():
   deleteSkins()
   return jsonify({'delete':'true'})

@files_api.route(API_PREFIX +'/', methods = ['POST'])
def zipdir():
    clean_dir()
    jsonfile = request.json
    JSONFILE = hydrate(jsonfile)
    write_json(JSONFILE)
    shutil.make_archive('./skins/Customs-'+jsonfile["racer"].lower()+'-'+str(jsonfile["number"]), 'zip', 'Customs')
    response = {'message': 'success'}
    return jsonify(response), 200
@files_api.route(API_PREFIX +'/get-files/<path:path>',methods = ['GET','POST'])
def get_files(path):

    """Download a file."""
    try:
        return send_from_directory(DOWNLOAD_PATH, path, as_attachment=True)
    except FileNotFoundError:
        abort(404,{"error":"File not found"})
      

@files_api.route(API_PREFIX +'/list/',methods=['GET'])
def listar():
   return jsonify(list_dir())

#ALIVE
@health_api.route(API_PREFIX + '/health/',methods=['GET'])
def isAlive():    
    return jsonify({"isAlive":"true"})