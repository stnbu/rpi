
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

GPIO.setup(32, GPIO.OUT)
GPIO.output(32, 0)

GPIO.output(32, 1)
raw_input('blah')
GPIO.cleanup()


