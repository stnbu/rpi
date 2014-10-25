
class Pin(object):

    def __init__(self, board, gpio=None):
        self.board = board
        self.gpio = gpio

class Board(object):

    def __init__(self, pins, version):
        self.pins = pins
        self.version = version


pins = [  # B+ pins
    Pin(board=3, gpio=2),
    Pin(board=5, gpio=3),
    Pin(board=7, gpio=4),
    Pin(board=8, gpio=14),
    Pin(board=10, gpio=15),
    Pin(board=11, gpio=17),
    Pin(board=12, gpio=18),
    Pin(board=13, gpio=27),
    Pin(board=15, gpio=22),
    Pin(board=16, gpio=23),
    Pin(board=18, gpio=24),
    Pin(board=19, gpio=10),
    Pin(board=21, gpio=9),
    Pin(board=22, gpio=25),
    Pin(board=23, gpio=11),
    Pin(board=24, gpio=8),
    Pin(board=26, gpio=7),
    Pin(board=29, gpio=5),
    Pin(board=31, gpio=6),
    Pin(board=32, gpio=12),
    Pin(board=33, gpio=13),
    Pin(board=35, gpio=19),
    Pin(board=36, gpio=16),
    Pin(board=37, gpio=26),
    Pin(board=38, gpio=20),
    Pin(board=40, gpio=21),
]

board = Board(pins=pins, version='B+')
