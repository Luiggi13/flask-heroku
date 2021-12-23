from os import abort, getcwd
import flask
from flask import jsonify, request, send_from_directory
from flask import Blueprint
import json
import requests
import imghdr
from handlers.compress import *
from handlers.custom_funcs import switch_statement
from models.model import carList, carNotFound


API_PREFIX = '/api/v1'
PATH_FILE = "%s/Customs/Cars/" % (getcwd())
UPLOAD_FOLDER = "%s/uploads/" % (getcwd())
DOWNLOAD_PATH = "%s/skins/" % (getcwd())
IMAGES_FOLDER = 'https://flask-h-deploy.herokuapp.com/api/v1/get-files/'

cars_api = Blueprint('cars_api', __name__)
apifile_api = Blueprint('apifile', __name__)
files_api = Blueprint('files_api', __name__)
health_api = Blueprint('health_api', __name__)
img_api = Blueprint('img_api', __name__)

#CARS ENDPOINT
@cars_api.route(API_PREFIX +'/cars/',methods=['GET'])
def listarCarsCompleted():    
    return jsonify(carList())

@cars_api.route(API_PREFIX +'/cars/<idCar>',methods=['GET'])
def listarCars(idCar):    
    for element in carList():
        if (str(element['id_car']) == idCar):
            return jsonify(element)
    return jsonify(carNotFound())

#FILES ENDPOINTS
@apifile_api.route(API_PREFIX +'/clear_all/',methods=['DELETE'])
def deleteFiles():
    deleteSkins()
    return jsonify({'delete':'true'})

@files_api.route(API_PREFIX +'/', methods = ['POST'])
def zipdir():
    clean_dir()
    JSONFILE = hydrate(request.json)
    write_json(JSONFILE)
    FILENAME = './skins/Customs-' + request.json["racer"].lower() + '-' + str(request.json["number"])
    shutil.make_archive(FILENAME, 'zip', 'Customs')
    return flask.send_file(FILENAME + '.zip',as_attachment=True)

@files_api.route(API_PREFIX +'/get-files/<path:path>',methods = ['GET','POST'])
def get_files(path):

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

#IMAGE PROCESSING TO REDUCE FILESIZE
@img_api.route(API_PREFIX + '/convert/',methods=['POST'])
def process_img():    
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            image.save(os.path.join(DOWNLOAD_PATH, image.filename))
            if switch_statement(imghdr.what(DOWNLOAD_PATH + image.filename)) == 0:
                return jsonify({"error":"Invalid file"})
        response = requests.post('http://api.resmush.it/ws.php?img='+IMAGES_FOLDER + image.filename,headers={"Content-Type":"application/json"})
    return jsonify({'msg': 'Image reduced', 'filename': json.loads(response.text)['dest']})