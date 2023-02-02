import cloudinary
import cloudinary.api
from cloudinary.uploader import upload
from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
# Camera warm-up time
sleep(2)
camera.capture('foo.jpg')

camera.stop_preview()

cloudinary.config(
    cloud_name = "dtzgeombx",
    api_key = "439128352662385",
    api_secret = "-4GUaMD9HH8hNldpI2kzI9eLiyU"
)

upload("foo2.jpg")
