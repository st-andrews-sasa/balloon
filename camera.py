import picamera
with picamera.PiCamera() as camera:
	camera.start_preview()
	camera.capture('image.png')

