#!/usr/bin/python
import subprocess
import RPi.GPIO as GPIO
import pipes
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
def main_loop ():
    global ch3status
    global ch2status
    input3 = GPIO.input(ch3)
    input2 = GPIO.input(ch2)
    if input3 == False:
        if ch3status != input3:
            handle=t.open('/home/pi/.config/pianobar/ctl','w')
            handle.write('p')
            handle.close()
    ch3status=input3
    if input2 == False:
        if ch2status != input2:
            handle=t.open('/home/pi/.config/pianobar/ctl','w')
            handle.write('n')
            handle.close()
    ch2status=input2
    if ch2status==False:
        if ch2status==ch3status:
            handle=t.open('/home/pi/.config/pianobar/ctl','w')
            handle.write('s')
            handle.write('10')
            handle.close()

while True:
    try:
        main_loop()
    except KeyboardInterrupt:
        process.terminate()
        print "Good bye"
