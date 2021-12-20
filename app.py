from flask import Flask, jsonify, request, send_from_directory
from zipfile import ZipFile
import shutil
from compress import *
from os import abort, getcwd
from flask_cors import CORS

PATH_FILE = "%s/Customs/Cars/" % (getcwd())
DOWNLOAD_PATH = "%s/skins/" % (getcwd())

app = Flask(__name__,static_url_path='')
CORS(app)
cors = CORS(app,resources={
    r"/*": {
        "origins":"*",
        "methods": ["OPTIONS", "GET", "POST"],
        "allow_headers": ["Authorization", "Content-Type"]
    }
})

@app.route('/', methods = ['POST'])
def zipdir():
    clean_dir()
    jsonfile = request.json
    JSONFILE = hydrate(jsonfile)
    write_json(JSONFILE)
    shutil.make_archive('./skins/Customs-'+jsonfile["racer"].lower()+'-'+str(jsonfile["number"]), 'zip', 'Customs')
    response = {'message': 'success'}
    return jsonify(response), 200
@app.route('/get-files/<path:path>',methods = ['GET','POST'])
def get_files(path):

    """Download a file."""
    try:
        return send_from_directory(DOWNLOAD_PATH, path, as_attachment=True)
    except FileNotFoundError:
        abort(404,{"error":"File not found"})
      

@app.route('/list/',methods=['GET'])
def listar():
   return jsonify(list_dir())

@app.route('/clear_all/',methods=['DELETE'])
def deleteFiles():
   deleteSkins()
   return jsonify({'delete':'true'})