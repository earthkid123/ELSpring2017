#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
def Blink():
  while(True):
    for i in range(0,3):
      print "blink #" + str(i+1)
      GPIO.output(17,True)
      time.sleep(0.10)
      GPIO.output(17,False)
      time.sleep(0.10)
    print ("Time to go take a 5 second nap")
    time.sleep(5)
    for i in range(0,4):
      print "blink #" + str(i+1)
      GPIO.output(17,True)
      time.sleep(0.10)
      GPIO.output(17,False)
      time.sleep(0.10)
  print ("Time for another 5 second nap")
  time.sleep(5)
  GPIO.cleanup()
Blink()
