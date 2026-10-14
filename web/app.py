from flask import Flask, send_from_directory

import os
import config
import logging

global DOCROOT
DOCROOT = "." # Overwritten by config

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

log = logging.getLogger(__name__)
app = Flask(__name__)


@app.route("/")
def hello():
    return "UOCIS docker demo!"

# https://stackoverflow.com/questions/45777770/catch-all-routes-for-flask
@app.route("/<path:path>")
def show_path(path):

    

    # https://flask.palletsprojects.com/en/stable/api/#flask.send_from_directory
    return send_from_directory(
        DOCROOT, path
    )




if __name__ == "__main__":
    options = config.configuration()
    assert options.DOCROOT, "Document root must be specified in configuration file credentials.ini or on command line"
    DOCROOT = options.DOCROOT
    port = options.PORT

    app.run(debug=True,host='0.0.0.0')
