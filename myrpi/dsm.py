import serial
import sys
import os
import curses


byte = None

def do_dsm():
    try:
        with serial.Serial(port='/dev/ttyAMA0', baudrate=115200, bytesize=8,
                           parity='N', stopbits=1, timeout=10) as ser:
            while byte != '\r':
                byte = ser.read(1)
                continue

            stdscr = curses.initscr()
            # next byte starts thing
            while True:
                bytes = []
                for x in range(16):
                    bytes.append(ser.read(1))

                if bytes[-1] != '\r':  # throw away frame that doesn't end with \r
                    continue

                s = ''
                for i, b in enumerate(bytes):
                    label = i
                    if label in (0,):
                        label = str(label) + '\trudder'
                    elif label in (11, 12):
                        label = str(label) + '\televator'
                    elif label in (13, 14):
                        label = str(label) + '\tgear'
                    elif label in (3, 4):
                        label = str(label) + '\tthrottle'
                    elif label in (9, 10):
                        label = str(label) + '\tflaps'
                    elif label in (7, 8):
                        label = str(label) + '\taileron'
                    else:
                        label = str(label) + '\t???????'
                    s += '{}:\t\t{:0=8b}\n'.format(label, ord(b))
                stdscr.addstr(0, 0, s)
                stdscr.refresh()

    except KeyboardInterrupt:
        pass

    finally:
        curses.endwin()

if __name__ == '__main__':
    do_dsm()
