#!/usr/bin/python3
"""Starts a Flask web application"""


from flask import Flask, render_template, make_response, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_session(self):
    """Closes current session"""
    storage.close()


@app.errorhandler(404)
def response_not_found(e):
    """
    handler for 404 errors that returns a JSON-formatted 404 status code
    response
    """
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", "5000")
    app.run(host, port, threaded=True)