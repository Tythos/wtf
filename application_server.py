"""
Defines a WSGI entry point (from Flask application) that can be used to host
the application by Passenger, when imported into *passenger_wsgi.py*. Can also
be invoked directly from the command line for development and testing purposes,
in which case it is hosted by gevent at localhost:8000.
"""

import os
import flask
from gevent import pywsgi

APP = flask.Flask("wtf")
SERVER_HOST = os.getenv("SERVER_HOST", "0.0.0.0")
SERVER_PORT = int(os.getenv("SERVER_PORT", "8000"))

@APP.route("/")
def index():
    """
    Root endpoint
    """
    lines = [
        b"This is a test!",
        b"If you can read this, Flask is successfully serving a WSGI application through Passenger.",
        b"This means you are awesome; congratulations!"
    ]
    return b"\n".join(lines), 200, {"Content-Type": "text/plain"}

def main():
    """
    By default, hosts locally w/ gevent on port 8000
    """
    pywsgi.WSGIServer((SERVER_HOST, SERVER_PORT), APP).serve_forever()

if __name__ == "__main__":
    main()
