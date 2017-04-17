import RPi.GPIO as GPIO
import time
import os
from get_char import _Getch
from definition import *
from movement_cam import *
from pdb import set_trace as bp


def set_servo(direction):
#	bp()
	global azimut, elevation
	global pre_azimut, pre_elevation
	if direction == 'r':
		azimut = azimut_up(azimut)
	elif direction == 't':
		azimut = azimut_down(azimut)
	elif direction == 'f':
		elevation = elevation_up(elevation)
	elif direction == 'g':
		elevation = elevation_down(elevation)
	else:
		q.stop()
		p.stop()
		GPIO.cleanup()
		return 'stop'
	
#	if elevation != pre_elevation:
#		q.ChangeFrequency(70)
#		enable_servo_elevation(elevation)
#	else:
#		q.ChangeFrequency(0.001)
#		disable_servo_elevation()
    		
#	if azimut != pre_azimut:
#		p.ChangeFrequency(70)
#		enable_servo_azimut(azimut)
#	else:
#		p.ChangeFrequency(0.001)
#		disable_servo_azimut()

	pre_elevation = elevation
	pre_azimut = azimut
   	p.ChangeDutyCycle(azimut)
 	q.ChangeDutyCycle(elevation)
	return 'ready'


def get_character():
	global start
	if start == 1:
		print "Insert a character: "
		print "r to move up and t to move down"
		print "f to move up and g to move down"
		start = 0
	direction = getch()
	state = set_servo(direction)
	return state

try:
	while True:
		state = get_character()
		if state == 'stop':
			break

except KeyboardInterrupt:
  p.stop()
  q.stop()
  GPIO.cleanup()
