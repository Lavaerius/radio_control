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
ch1status=True
combo1=False
combo2=False
combo3=False
combo4=False
def write_ctl (commands_list):
    for i in commands_list:
        handle=t.open('/home/pi/.config/pianobar/ctl','w')
        print i
        handle.write(i)
        handle.close()

def main_loop ():
    global ch3status
    global ch2status
    global ch1status
    global combo1
    global combo2
    global combo3
    global combo4
    input3 = GPIO.input(ch3)
    input2 = GPIO.input(ch2)
    input1 = GPIO.input(ch1)
    if input3 == False and ch3status != input3:
        write_ctl("p")
    ch3status=input3
    if input2 == False and ch2status != input2:
        write_ctl("n")
    ch2status=input2
    if combo1==False:
        if input2==False and input3==False:
            combo1=True
            print combo1
            write_ctl(["s10","\n"])
            time.sleep(0.05)
    ch2status=input2
    ch3status=input3
    if input2 != input3:
        combo1=False
        
    if combo2==False:
        if ch1status==False and ch3status==False:
            combo2=True
            write_ctl(["s11","\n"])
            time.sleep(0.05)
    ch1status=input1
    ch3status=input3
    if ch1status != ch3status:
        combo1=False

    if combo3==False:
        if ch2status==False and ch1status==False:
            combo3=True
            write_ctl(["s12","\n"])
            time.sleep(0.05)
    ch2status=input2
    ch1status=input1
    if ch2status != ch1status:
        combo3=False
        
    if combo4==False:
        if ch2status==False and ch3status==False and ch1status==False:
            combo4=True
            write_ctl(["s13","\n"])
            time.sleep(0.05)
    ch2status=input2
    ch3status=input3
    ch1status=input1
    if ch2status != ch3status or ch2status != ch1status or ch3status != ch1status:
        combo4=False    
        
        
while True:
    try:
        main_loop()
    except KeyboardInterrupt:
        process.terminate()
        print "Good bye"
