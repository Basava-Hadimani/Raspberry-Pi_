import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.OUT)


while True :
    print("the light1 s on")
    GPIO.output(13,True)
    time.sleep(5)
    print("the light1 is  off")
    GPIO.output(13,False)


    
GPIO.cleanup()

