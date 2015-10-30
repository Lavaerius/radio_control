#!/usr/bin/python
import subprocess
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
cmd = ["/usr/local/bin/pianobar"]
process = subprocess.Popen(cmd)
print process.pid
ch1 = 1
ch2 = 2
ch3 = 3
volup=4
voldown=5
GPIO.setmode(GPIO.BCM)
GPIO.setup(ch1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ch2,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ch3,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(volup,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(voldown,GPIO.IN, pull_up_down=GPIO.PUD_UP)

def main_loop ():
        print "adasdsasa"
        print process.pid


try:
 while 1:
        main_loop
except KeyboardInterrupt:
    process.terminate()
    print "Good bye"
