from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

def simple_app(environ, start_response):
    setup_testing_defaults(environ)
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)
    ret = ["%s: %s\n" % (key, value) for key, value in environ.iteritems()]
    return ret

def run(app):
    httpd = make_server('0.0.0.0', 8000, app)
    httpd.serve_forever()

