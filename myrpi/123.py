
import RPi.GPIO as GPIO
from random import randint
from time import sleep
import os
from wave import open as waveOpen
from ossaudiodev import open as ossOpen
try:
    from ossaudiodev import AFMT_S16_NE
except ImportError:
    if byteorder == "little":
        AFMT_S16_NE = ossaudiodev.AFMT_S16_LE
    else:
        AFMT_S16_NE = ossaudiodev.AFMT_S16_BE

def three():
    s = waveOpen(os.path.join(os.path.dirname(__file__), '1.wav'), 'rb')
    nc, sw, fr, nf, comptype, compname = s.getparams()
    dsp = ossOpen('/dev/dsp','w')
    dsp.setparameters(AFMT_S16_NE, nc, fr)
    data = s.readframes(nf)
    s.close()
    dsp.write(data)
    dsp.close()

GPIO.setmode(GPIO.BOARD)


RED = 33
BLUE2 = 32
GREEN = 35
BLUE = 37

pins = RED, BLUE, BLUE2, GREEN, 18

for color in pins:
    GPIO.setup(color, GPIO.OUT)
    GPIO.output(color, 0)

try:
    while True:
        for pin in pins:
            GPIO.output(pin, randint(0, 1))
        #sleep(0.5)
        three()
except KeyboardInterrupt:
    GPIO.cleanup()


