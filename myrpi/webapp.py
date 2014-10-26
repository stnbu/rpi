
import os
import sys
import daemon
from daemon.pidlockfile import PIDLockFile
from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server
import www

DIR_PATH = os.path.join(os.path.sep, 'tmp', 'raspiweb')
LOG_PATH = os.path.join(DIR_PATH, 'raspiweb.log')
PID_PATH = os.path.join(DIR_PATH, 'pid')


def raspiweb(environ, start_response):
    setup_testing_defaults(environ)

    status = '200 OK'
    headers = [('Content-type', 'text/plain')]

    start_response(status, headers)

    ret = ["%s: %s\n" % (key, value)
           for key, value in environ.iteritems()]
    return ret

def start(app):
    if not os.path.exists(DIR_PATH):
        os.makedirs(DIR_PATH)
    if os.path.exists(PID_PATH):
        print >>sys.stderr, '{0}: File exists. Already running?'.format(PID_PATH)
        sys.exit(1)

    pid_file = PIDLockFile(PID_PATH)
    log_file = open(LOG_PATH, 'a')
    with daemon.DaemonContext(pidfile=pid_file, stdout=log_file, stderr=log_file):
        httpd = make_server('0.0.0.0', 8000, app)
        httpd.serve_forever()

APP = raspiweb

def stop():
    global PID_PATH
    SIGTERM = 15
    try:
        os.kill(int(open(PID_PATH, 'r').read()), SIGTERM)
    except IOError:
        print >>sys.stderr, '{0}: no such file. Not running?'.format(PID_PATH)
        sys.exit(1)

def main():
    if len(sys.argv) == 2:
        _, cmd = sys.argv
    else:
        cmd = 'start'
    cmd = cmd.lower()

    if cmd == 'start':
        start(raspiweb)
    elif cmd == 'stop':
        stop()
    elif cmd == 'restart':
        stop()
        start(raspiweb)
    else:
        raise ValueError('Unknown subcommand "{0}"'.format(cmd))

if __name__ == '__main__':
    main()
