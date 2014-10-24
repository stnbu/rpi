
import RPi.GPIO as GPIO
from random import randint
from time import sleep


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
        sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()

