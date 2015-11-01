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
handle=t.open('/home/pi/.config/pianobar/ctl','w')
ch3status=True
burp=open("/home/pi/dummy","w")
handle.write("n")
def main_loop ():
    global ch3status
    input = GPIO.input(ch3)
    if input == False:
        if ch3status != input:
            ch3status=input
            handle.write('p')
            burp.write("asdflkjasdlaskjdas")


while True:
    try:
        main_loop()
    except KeyboardInterrupt:
        handle.close()
        process.terminate()
        print "Good bye"
