import RPi.GPIO as GPIO
import time

BUZZ_PIN = 33
BUTTON_PIN = 40
LED_PIN = 32
SHOCK_PIN = 29

GPIO.setmode(GPIO.BOARD)

def buzz(pin):
    GPIO.output(BUZZ_PIN, 1)
    time.sleep(0.5)
    GPIO.output(BUZZ_PIN, 0)

def led(pin):
    GPIO.output(LED_PIN, 1)
    time.sleep(2.0)
    GPIO.output(LED_PIN, 0)

time.sleep(1)

print 'Press button for service.'

try:
    GPIO.setup(BUZZ_PIN, GPIO.OUT)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.setup(BUTTON_PIN, GPIO.IN)
    GPIO.setup(SHOCK_PIN, GPIO.IN)

    GPIO.add_event_detect(BUTTON_PIN, GPIO.RISING, callback=led)
    GPIO.add_event_detect(SHOCK_PIN, GPIO.RISING, callback=buzz)
    while 1:
        time.sleep(100)
except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
