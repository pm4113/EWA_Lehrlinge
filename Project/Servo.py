import RPi.GPIO as GPIO
import time
import os
from get_char import _Getch
from pdb import set_trace as bp
#os.system("raspivid -o - -t 0 -n -vf -hf -w 1280 -h 720 -fps 25 -g 100 | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/,mux=ts}' :demux=h264") 


servoPIN_1 = 27
EnablePIN_1 = 5
servoPIN_2 = 6
EnablePIN_2 = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN_1, GPIO.OUT)
GPIO.setup(servoPIN_2, GPIO.OUT)
GPIO.setup(EnablePIN_1, GPIO.OUT)
GPIO.setup(EnablePIN_2, GPIO.OUT)
GPIO.output(EnablePIN_1, 1)
GPIO.output(EnablePIN_2, 1)

p = GPIO.PWM(servoPIN_1, 50) # GPIO 17 als PWM mit 50Hz
q = GPIO.PWM(servoPIN_2, 50)

cycle_channel = 0
p.start(cycle_channel) # Initialisierung
q.start(cycle_channel)

getch = _Getch() 	# call class _Getch() from import file get_char

print "Insert a character: "


def DC_up():
	DC_up.cycle_channel += 0.002
#    q.ChangeDutyCycle(2.5)
#    time.sleep(0.5)
#	time.sleep(0.05)
	return DC_up.cycle_channel

def DC_down():
	DC_down.cycle_channel -= 0.002
	if DC_down.cycle_channel <=0:
		DC_down.cycle_channel = 0
	return DC_down.cycle_channel

DC_up.cycle_channel = 0
DC_down.cycle_channel = 0

cycle = 1
try:
	while True:
		direction = getch()
		bp()	
		if direction == 'q':
			print direction
			cycle = DC_up()
		elif direction == 'e':
			print direction
			cycle = DC_down()
		else:
			break
     		
     		p.ChangeDutyCycle(cycle)
    	 	q.ChangeDutyCycle(cycle)

except KeyboardInterrupt:
  	p.stop()
  	q.stop()
  	GPIO.cleanup()
