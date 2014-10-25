import serial
import sys
import os
import curses


byte = None

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

            if bytes[-1] != '\r':  # throw away
                continue

            s = ''
            for i, b in enumerate(bytes):
                s += '{0}: {1}\n'.format(i, repr(b))
            stdscr.addstr(0, 0, s)
            stdscr.refresh()

except KeyboardInterrupt:
    pass
finally:
    curses.endwin()

