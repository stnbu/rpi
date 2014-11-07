import serial
import curses
import calibration

def get_channel_data(bytes):
    for index, byte in enumerate(bytes):
        if index % 2:  # if an odd member
            channel_id = last & 0b11111100
            channel_id = channel_id >> 2  # first two bits are for something else
            last = last & 0b00000011  # mask the first 6 bits
            last = last << 8
            position = byte | last  # "append" byte to the last byte
            yield channel_id, position
        last = byte


def format_channel_data(data):
    for channel_id, position in data:
        axis = calibration.data[channel_id]
        yield channel_id, axis.get_normalized_position(position)

class Handler(object):
    """Should have __call__, setup, and cleanup methods.
    """


class Visualizer(Handler):

    def setup(self):
        self.stdscr = curses.initscr()

    def __call__(self, channel_data):
        s = ''
        for channel_id, position in channel_data:
            s += 'c: {0} {1}\t{2}\n'.format(channel_id, calibration.data[channel_id].name, position)
        s += '\n'
        s += '=' * 120
        self.stdscr.addstr(0, 0, s)
        self.stdscr.refresh()

    def cleanup(self):
        curses.endwin()


def do_dsm(port, handler=Visualizer()):

    with serial.Serial(port=port, baudrate=115200, bytesize=8, parity='N', stopbits=1) as ser:

        byte = None

        while byte != '\r':  # read, discard first frame
            byte = ser.read(1)
            continue

        handler.setup()

        while True:
            try:
                bytes = []
                for x in range(16):
                    bytes.append(ser.read(1))

                bytes = bytes[-1:] + bytes[:-1]
                bytes = map(ord, bytes)

                channel_data = get_channel_data(bytes)
                channel_data = format_channel_data(channel_data)

                handler(channel_data)

            except KeyboardInterrupt:
                break

        handler.cleanup()

if __name__ == '__main__':
    do_dsm(port='/dev/ttyUSB0')
