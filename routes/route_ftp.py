from os import abort, getcwd
import flask
from flask import jsonify, request, send_from_directory
from flask import Blueprint
import json
import requests
import imghdr
from handlers.compress import *
from handlers.custom_funcs import callLaps, lapTime, switch_statement
from models.model import carList, carNotFound
import ftplib

API_PREFIX = "/api/v1"
RESULTS_PATH = "%s/results/" % (getcwd())
HOSTNAME = "es2.assettohosting.com"
USERNAME = "mercedes2"
PASSWORD = "red"

ftp_api = Blueprint("ftp_api", __name__)

# CARS ENDPOINT
@ftp_api.route(API_PREFIX + "/ftp/", methods=["GET"])
def ftp_call():
  OK =  '_fp'
  ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
  ftp_server.encoding = "utf-8"
  tete = ftp_server.nlst()
  for element in tete:
    if OK.lower() in element.lower():
      filename = element
      # Write file in binary mode
      with open(RESULTS_PATH + filename, "wb") as file:
      # Command for Downloading the file "RETR filename"
        ftp_server.retrbinary(f"RETR {filename}", file.write)
  ftp_server.quit()
  return jsonify({"success":"true"})

