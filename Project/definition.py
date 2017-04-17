import RPi.GPIO as GPIO
from get_char import _Getch
#os.system("raspivid -o - -t 0 -n -vf -hf -w 1280 -h 720 -fps 25 -g 100 | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/,mux=ts}' :demux=h264") 

GPIO.setwarnings(False)
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

p = GPIO.PWM(servoPIN_1, 70) # GPIO 17 als PWM mit 50Hz
q = GPIO.PWM(servoPIN_2, 70)

start = 1
azimut = 0 
elevation = 0
pre_azimut = 0
pre_elevation = 0

p.start(azimut) # Initialisierung
q.start(elevation)

getch = _Getch()        # call class _Getch() from import file get_char

azimut = 0
elevation = 0

def enable_servo_azimut(azimut):
	p.ChangeFrequency(70)

def disable_servo_azimut():
	p.ChangeFrequency(0.1)

def enable_servo_elevation(elevation):
	p.ChangeFrequency(70)

def disable_servo_elevation():
	p.ChangeFrequency(0.1)



