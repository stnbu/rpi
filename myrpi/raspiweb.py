import os
from lxml import etree
import wsgiref
from StringIO import StringIO

BASE = os.path.join(os.path.dirname(__file__), '..', 'web')
BASE = os.path.abspath(BASE)
assert os.path.exists(BASE)

class RaspiWeb(object):

    def get_html_header(self, title_text=''):
        head = etree.Element('head')
        title = etree.Element('title')
        title.text = title_text
        head.append(title)
        if False:
            meta = etree.Element('meta', http_equiv='Content-Type', content='text/html', charset='UTF-8')
            head.append(meta)
            meta = etree.Element('meta', http_equiv='Content-Style-Type', content='text/css')
            head.append(meta)
            css = etree.Element('link', rel='stylesheet', href='/sencss/source/sen.css', type='text/css')
            head.append(css)
            script = etree.Element('script', src='/jquery/src/jquery.js', type='text/javascript')
            head.append(script)
        return head

    def get_html_body(self, pretty_print=True):
        html = etree.Element('html')
        head = self.get_html_header()
        html.append(head)
        body = etree.Element('body')
        p = etree.Element('p')
        p.text = 'FDSAFDSAFDSFDAFAFADFAF'
        body.append(p)
        body.append(etree.Element('hr'))
        env = etree.Element('pre')
        env.text = '\n'.join(["%s: %s" % (key, value) for key, value in self.current_environ.iteritems()])
        body.append(env)
        html.append(body)
        doctype = """<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN\""""
        return etree.tostring(html, doctype=doctype, pretty_print=pretty_print)

    def __call__(self, environ, start_response):

        self.current_environ = environ

        environ.setdefault('SERVER_NAME', '0.0.0.0')
        environ.setdefault('SERVER_PROTOCOL', 'HTTP/1.0')
        environ.setdefault('HTTP_HOST', environ['SERVER_NAME'])
        environ.setdefault('REQUEST_METHOD', 'GET')
        if 'SCRIPT_NAME' not in environ and 'PATH_INFO' not in environ:
            environ.setdefault('SCRIPT_NAME', '')
            environ.setdefault('PATH_INFO', '/')
        environ.setdefault('wsgi.run_once', 0)
        environ.setdefault('wsgi.multithread', 0)
        environ.setdefault('wsgi.multiprocess', 0)
        environ.setdefault('wsgi.input', StringIO(""))
        environ.setdefault('wsgi.errors', StringIO())
        environ.setdefault(
            'wsgi.url_scheme', wsgiref.util.guess_scheme(environ))
        if environ['wsgi.url_scheme'] == 'http':
            environ.setdefault('SERVER_PORT', '80')
        elif environ['wsgi.url_scheme'] == 'https':
            environ.setdefault('SERVER_PORT', '443')
        status = '200 OK'
        headers = [('Content-type', 'text/html')]
        start_response(status, headers)

        if not environ['PATH_INFO'].startswith('/'):
            raise ValueError('{0}: We only deal in absolute URIs at the moment.'.format(environ['PATH_INFO']))

        response = self.get_html_body()
        return response
