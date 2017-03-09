#!/usr/bin/python
import os
import time
import sqlite3
import sys
""" Log Current Time, Temperature in Celsius and Fahrenheit
Returns a list [time, tempC, tempF] """
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

def readTemp():
        tempfile = open("/sys/bus/w1/devices/28-0416862076ff/w1_slave")
        tempfile_text = tempfile.read()
        currentTime=time.strftime('%x %X %Z')
        tempfile.close()
        tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000
        tempF=tempC*9.0/5.0+32.0
        return [currentTime, tempC, tempF]
while True:
 print(readTemp())
        time.sleep(30)
