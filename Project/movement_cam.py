import sys
import time
import threading
from definition import *

global PWM_time

class TimerClass(threading.Thread):

	def __init__(self):
		threading.Thread.__init__(self)
		self.event = threading.Event()

	def run(self):
		while not self.event.is_set():
			print(time.time())
			self.event.wait( PWM_time )

	def stop(self):
		self.event.set()

tmr = TimerClass()

def starttime():
	tmr.start()

def stoptime():
	tmr.stop()


def azimut_up(dc_azimut):
        dc_azimut += 1
        if dc_azimut >= 30:
                dc_azimut = 30
        print "DC_UP_AZI: " + str(dc_azimut)
        return dc_azimut

def azimut_down(dc_azimut):
        dc_azimut -= 1
        if dc_azimut <= 0:
                dc_azimut = 0
        print "DC_DOWN_AZI: " + str(dc_azimut)
        return dc_azimut

def elevation_up(dc_elevation):
        dc_elevation += 1
        if dc_elevation >= 30:
                dc_elevation = 30
        print "DC_UP_ELEV: " + str(dc_elevation)
        return dc_elevation

def elevation_down(dc_elevation):
        dc_elevation -= 1
        if dc_elevation <= 0:
                dc_elevation = 0
        print "DC_DOWN_ELEV: " + str(dc_elevation)
        return dc_elevation
