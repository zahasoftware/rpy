# Ref https://www.raspberrypi.org/documentation/usage/camera/python/README.md
import picamera
from time  import sleep 

class Camera(object):
    """ picamera Wrapper Class """

    def __init__(self):
        self.camera = picamera.PiCamera()

    def TakePicture(self, path, preview_timeout=2):
        self.camera.start_preview()
        sleep(preview_delay)

        selft.capture(path)
        self.camera.stop_preview()
        
