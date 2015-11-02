#!/usr/bin/python
import subprocess
import RPi.GPIO as GPIO
import pipes
import time
from array import *
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
t=pipes.Template()
#t.append('tr a-z A-Z','--')
ch3status=True
ch2status=True
combo1=False

def write_ctl (commands_list):
    for i in commands_list:
        handle=t.open('/home/pi/.config/pianobar/ctl','w')
        handle.write(i)
        handle.close()

def main_loop ():
    global ch3status
    global ch2status
    global combo1
    input3 = GPIO.input(ch3)
    input2 = GPIO.input(ch2)
    if input3 == False and ch3status != input3:
        write_ctl("p")
    ch3status=input3
    if input2 == False and ch2status != input2:
        write_ctl("n")
    ch2status=input2

    if combo1==False:
        if ch2status==False and ch3status==False:
            combo1=True
            write_ctl(["s10","\n"])
            time.sleep(0.05)
    ch2status=input2
    ch3status=input3
    if ch2status != ch3status
        combo1=False

while True:
    try:
        main_loop()
    except KeyboardInterrupt:
        process.terminate()
        print "Good bye"
