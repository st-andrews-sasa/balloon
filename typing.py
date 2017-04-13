from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)
while 1:
	red = (255, 0, 0)
	sense.show_message(input(), text_colour=red, scroll_speed=0.07)
