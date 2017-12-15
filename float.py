import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.IN)
while True:
	if(GPIO.input(13)==1):
		print"water is full"
		time.sleep(2)
	else:
		print"water is empty"
		time.sleep(1)
GPIO.cleanup()
