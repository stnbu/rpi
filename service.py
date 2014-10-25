import RPi.GPIO as GPIO
import time

BUZZ_PIN = 33
BUTTON_PIN = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUZZ_PIN, GPIO.OUT)

def buzz(pin):
    GPIO.output(BUZZ_PIN, 1)
    time.sleep(0.5)
    GPIO.output(BUZZ_PIN, 0)

time.sleep(1)

print 'Press button for service.'

try:
    GPIO.setup(BUTTON_PIN, GPIO.IN)
    GPIO.add_event_detect(BUTTON_PIN, GPIO.RISING, callback=buzz)
    while 1:
        time.sleep(100)
except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
