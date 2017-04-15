import RPi.GPIO as GPIO
import time

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
p.start(2.5) # Initialisierung
q.start(2.5)
try:
  while True:
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(2.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(2.5)
    time.sleep(0.5)

except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
