
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)

b = True
while True:
    GPIO.output(12, int(b))
    b = not b
    print 'xxxxx', int(b),
    raw_input('')

GPIO.cleanup()

