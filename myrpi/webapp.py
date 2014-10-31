
import os
import sys
import daemon
import argparse
from daemon.pidlockfile import PIDLockFile
from wsgiref.simple_server import make_server
from raspiweb import raspiweb

DEFAULT_OUT_PATH = os.path.join(os.path.sep, 'tmp', 'raspiweb')

def get_pid_path(args):
    return os.path.join(args.out_dir, 'pid')

def get_log_path(args):
    return os.path.join(args.out_dir, 'log')

def start(app, args):
    if not os.path.exists(args.out_dir):
        os.makedirs(args.out_dir)
    if os.path.exists(get_pid_path(args)):
        if args.ignore_stale_pid:
            os.remove(get_pid_path(args))
        else:
            print >>sys.stderr, '{0}: File exists. Already running?'.format(get_pid_path(args))
            sys.exit(1)

    pid_file = PIDLockFile(get_pid_path(args))
    log_file = open(get_log_path(args), 'a')

    def run():
        httpd = make_server('0.0.0.0', 8000, app)
        httpd.serve_forever()

    if not args.foreground:
        with daemon.DaemonContext(pidfile=pid_file, stdout=log_file, stderr=log_file):
            run()
    else:
        run()

def get_parser():

    parser = argparse.ArgumentParser(description='Run an WSGI application')

    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', default=False)
    parser.add_argument('-d', '--out-dir', dest='out_dir', metavar='output_directory', default=DEFAULT_OUT_PATH,
                        help='Direcotry for logs, PID file, etc.',)

    mode = parser.add_subparsers(dest="mode")

    class Args(object):
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

    # args re-used in different subparsers
    foreground = Args('-F', '--foreground', action='store_true', default=False)
    ignore_pid = Args('-i', '--ignore-stale-pid', action='store_true', default=False)
    force = Args('-f', '--force', action='store_true', default=False)

    start = mode.add_parser('start')
    start.add_argument(*foreground.args, **foreground.kwargs)
    start.add_argument(*ignore_pid.args, **ignore_pid.kwargs)

    stop = mode.add_parser('stop')
    stop.add_argument(*force.args, **force.kwargs)

    restart = mode.add_parser('restart')
    restart.add_argument(*foreground.args, **foreground.kwargs)
    restart.add_argument(*ignore_pid.args, **ignore_pid.kwargs)
    restart.add_argument(*force.args, **force.kwargs)

    return parser


APP = raspiweb

def stop(args):

    SIGTERM = 15
    SIGKILL = 9
    try:
        os.kill(int(open(get_pid_path(args), 'r').read()), SIGTERM)
    except IOError:
        pass
    except Exception:
        if args.force:
            os.kill(int(open(get_pid_path(args), 'r').read()), SIGKILL)

def main():

    args = get_parser().parse_args()

    if args.mode == 'start':
        start(raspiweb, args)
    elif args.mode == 'stop':
        stop(args)
    elif args.mode == 'restart':
        stop(args)
        start(raspiweb, args)
    else:
        raise ValueError('Unknown subcommand "{0}"'.format(args.mode))

if __name__ == '__main__':
    main()
