from pygame import camera
from pygame import image
camera.init()
cam = camera.Camera(camera.list_cameras()[0])
cam.start()
img = cam.get_image()
image.save(img, "/tmp/photo.bmp")
camera.quit()
