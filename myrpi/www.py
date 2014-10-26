from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

def run(app):
    httpd = make_server('0.0.0.0', 8000, app)
    httpd.serve_forever()

