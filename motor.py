import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
pins=[15,16,18,19]
for p in pins:
    GPIO.setup(p,GPIO.OUT)
    GPIO.output(p,0)
seq=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
seq1=[[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]
print"1-clockwise and 2-anticlockwise"
n=int(input("enter the number"))
if n==1:
      for i in range (512):
        for fullstep in range(4):
            for p in range(4):
                GPIO.output(pins[p],seq[fullstep][p])
                time.sleep(0.001)
      print "end of clockwise direction"          
else:
    for i in range (512):
        for fullstep in range(4):
            for p in range(4):
                GPIO.output(pins[p],seq1[fullstep][p])
                time.sleep(0.001)
    print "end of anticlockwise directon"        
GPIO.cleanup()
                
                
    
