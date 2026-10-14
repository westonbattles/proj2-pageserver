from flask import Flask, send_from_directory

import os
import config
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

log = logging.getLogger(__name__)
app = Flask(__name__)

global DOCROOT
DOCROOT = "." # Overwritten by config

ALLOWED_EXTENSIONS = {".html", ".css"}
FORBIDDEN_URL_SUBSTRINGS = {"/~", "//", "/.."} #prepend with / to represent start of the name of a page, as per the instructions of the assignment
FORBIDDEN_URL_SUBSTRINGS.add("~")


@app.route("/")
def hello():
    return "UOCIS docker demo!"

# https://stackoverflow.com/questions/45777770/catch-all-routes-for-flask
@app.route("/<path:path>")
def show_path(path):

    # make sure we don't have a forbidden substring in our midst
    for substring in FORBIDDEN_URL_SUBSTRINGS:
        if substring in "/" + path: # https://www.geeksforgeeks.org/python/check-if-string-contains-substring-in-python/
            return send_from_directory(DOCROOT,"403.html"), 403

    # make sure extension is either .html or .css
    split_path_ext = os.path.splitext(path) # https://www.geeksforgeeks.org/python/how-to-get-file-extension-in-python/
    if split_path_ext[1] not in ALLOWED_EXTENSIONS:
        return send_from_directory(DOCROOT,"403.html"), 403

    # https://flask.palletsprojects.com/en/stable/api/#flask.send_from_directory
    return send_from_directory(
        DOCROOT, path
    )


@app.errorhandler(404)
def handle_404(e):
    return send_from_directory(DOCROOT,"404.html"), 404




if __name__ == "__main__":
    options = config.configuration()
    assert options.DOCROOT, "Document root must be specified in configuration file credentials.ini or on command line"
    DOCROOT = options.DOCROOT
    port = options.PORT

    app.run(debug=True,host='0.0.0.0')
