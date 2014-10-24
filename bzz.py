
import RPi.GPIO as GPIO
from random import randint
from time import sleep


GPIO.setmode(GPIO.BOARD)

GPIO.setup(33, GPIO.OUT)
GPIO.output(33, 0)
raw_input('one...')
GPIO.output(33, 1)
raw_input('zero...')
GPIO.output(33, 0)
raw_input('cleanup.')
GPIO.cleanup()

