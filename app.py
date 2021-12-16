from flask import Flask, jsonify, request
from zipfile import ZipFile
import shutil
from compress import *
from os import getcwd

PATH_FILE = "%s/Customs/Cars/" % (getcwd())

app = Flask(__name__)

@app.route('/',methods = ['POST'])
def zipdir():
    # content_type = request.headers.get('Content-Type')
    clean_dir()
    jsonfile = request.json
    JSONFILE = hydrate(jsonfile)
    write_json(JSONFILE)
    shutil.make_archive('Customs', 'zip', 'Customs')
    response = {'message': 'success'}
    return jsonify(response), 200