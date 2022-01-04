from flask import Flask
from flask_cors import CORS
from routes.routes import *
from routes.route_ftp import *

app = Flask(__name__, static_url_path="")
app.register_blueprint(cars_api)
app.register_blueprint(apifile_api)
app.register_blueprint(files_api)
app.register_blueprint(health_api)
app.register_blueprint(img_api)
app.register_blueprint(ftp_api)
CORS(app)

cors = CORS(
    app,
    resources={
        r"/*": {
            "origins": "*",
            "methods": ["OPTIONS", "GET", "POST"],
            "allow_headers": ["*"],
        }
    },
)
