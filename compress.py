from flask import jsonify
import json
import os, shutil
from os import getcwd

PATH_FILE = "%s/Customs/Cars/" % (getcwd())
SKINS_FOLDER = "%s/skins/" % (getcwd())
URL = "https://flask-h-deploy.herokuapp.com/get-files/"

def hydrate(jsonObj: dict):
  filename = "test.json"
  customJson = {
    "name": jsonObj["racer"],
    "number": jsonObj["number"]
  }
  if 'team' in jsonObj:
    customJson['team'] = jsonObj['team']
  return customJson

def write_json(data, filename="custom.json"):
  print(PATH_FILE + data["name"]+ "-" +str(data["number"]) +'.json')
  with open(PATH_FILE + data["name"].lower()+ "-" +str(data["number"]) +'.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

def clean_dir():
  for filename in os.listdir(PATH_FILE):
      file_path = os.path.join(PATH_FILE, filename)
      try:
          if os.path.isfile(file_path) or os.path.islink(file_path):
              os.unlink(file_path)
          elif os.path.isdir(file_path):
              shutil.rmtree(file_path)
      except Exception as e:
          print('Failed to delete %s. Reason: %s' % (file_path, e))

def list_dir():
  count = 0;
  data = {'total_files':0,'all_files': None}
  files = []
  href:str='href';
  
  for filename in os.listdir(SKINS_FOLDER):
      file_path = os.path.join(SKINS_FOLDER, filename)
      try:
          if os.path.isfile(file_path) or os.path.islink(file_path):
              print(file_path)
              files.append({href:URL + filename})
      except Exception as e:
          print('Failed to delete %s. Reason: %s' % (file_path, e))
  data['total_files'] = len(files)
  data['all_files'] = files
  return data
def deleteSkins():
  files = []
  for filename in os.listdir(SKINS_FOLDER):
      file_path = os.path.join(SKINS_FOLDER, filename)
      try:
          if os.path.isfile(file_path) or os.path.islink(file_path):
            
              os.unlink(file_path)
      except Exception as e:
          print('Failed to delete %s. Reason: %s' % (file_path, e))