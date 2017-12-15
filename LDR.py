import RPi.GPIO as GPIO
import time
GPIO.setwarnings(0)
ldr=26
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ldr,GPIO.IN)
GPIO.setup(19,GPIO.OUT)
GPIO.output(19,0)
print ldr.value
while True:
    if (GPIO.input(26)==0):
        GPIO.output(19,1)
        time.sleep(2)
        print 'danger'
    else:
         GPIO.output(19,0)
GPIO.cleanup()

        
