import picamera
from time import sleep
sleep(5)
camera = picamera.PiCamera()
print 'img'
camera.capture('/tmp/image.jpg')
print 'vid'
camera.start_recording('/tmp/video.h264')
sleep(5)
camera.stop_recording()
