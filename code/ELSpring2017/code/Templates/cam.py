import RPi.GPIO as GPIO
from flask import Flask, render_template, request, redirect, url_for
import time
#from SimpleCV import Camera
#sudo apt-get install python-opencv
from picamera import PiCamera
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096


#camera.start_preview()
#sleep(10)
#camera.stop_preview()

app = Flask(__name__, template_folder='../Templates')

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(0, GPIO.OUT)  
#pwm1 = GPIO.PWM(0, 50)  
#pwm1.start(5)  
#GPIO.setup(1, GPIO.OUT)  
#pwm2 = GPIO.PWM(1, 50)  
#pwm2.start(7.5)  


@app.route("/")
def main():
    templateData={
        'x' : 0 ,
        'y' : 0,
        'deg': 10,
        }
    return render_template('index.html', **templateData)
    


@app.route("/move", methods = ['POST', 'GET'])
x=request.form('x')
#dx2=1./18.*(x)+2
#pwm1.ChangeDutyCycle(dx2)
#time.sleep(1)
y=request.form('y')
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
    pwm.set_pwm_freq(60)

    print('Moving servo on channel 0, press Ctrl-C to quit...')
    # Move servo on channel O between extremes.
    pwm.set_pwm(0, 0, servo_min)
    time.sleep(1)
    pwm.set_pwm(0, 0, servo_max)
    time.sleep(1)
    pwm.set_pwm(2, 2, servo_min)
    time.sleep(1)
    pwm.set_pwm(2, 2, servo_max)
    time.sleep(1)
    return render_template('index.html')

@app.route("/reset")
def reset():
    dx2=1./18.*(0)+2
    pwm1.ChangeDutyCycle(dx2)    
    time.sleep(1)
    return render_template('index.html')


@app.route("/capture", methods = ['POST', 'GET'])
def capture():
    camera = PiCamera()
    camera.start_preview()
    sleep(2)
    camera.capture('/home/pi/Desktop/img/i.jpg')
    camera.stop_preview()
    return render_template('index.html')
   
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
