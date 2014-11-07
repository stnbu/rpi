import serial
import curses

def format_channel_data(bytes):
    for index, byte in enumerate(bytes):
        if index % 2:  # if an odd member
            channel_id = last & 0b11111100
            last = last & 0b00000011  # mask the first 6 bits
            last = last << 8
            position = byte | last  # "append" byte to the last byte
            yield channel_id, position
        last = byte


def do_dsm():

    with serial.Serial(port='/dev/ttyUSB0', baudrate=115200, bytesize=8, parity='N', stopbits=1) as ser:

        byte = None

        while byte != '\r':  # read, discard first frame
            byte = ser.read(1)
            continue

        stdscr = curses.initscr()

        while True:
            try:
                bytes = []
                for x in range(16):
                    bytes.append(ser.read(1))

                bytes = bytes[-1:] + bytes[:-1]
                bytes = map(ord, bytes)

                channel_data = format_channel_data(bytes)

                s = ''
                for channel_id, position in channel_data:
                    s += 'c: {0}\t{1}\n'.format(channel_id, position)
                s += '\n'
                s += '=' * 120

                stdscr.addstr(0, 0, s)
                stdscr.refresh()

            except KeyboardInterrupt:
                curses.endwin()
                break

        curses.endwin()

if __name__ == '__main__':
    do_dsm()
