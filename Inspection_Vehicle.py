import board
import neopixel
import datetime
import time
import os
import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False);

GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)

GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

PWM_A = GPIO.PWM(21, 100) #left engine
PWM_B = GPIO.PWM(6, 100) #right engine

PWM_A.start(0)
PWM_B.start(0)

def START_ENGINE():
	GPIO.output(16, GPIO.LOW)
	GPIO.output(20, GPIO.HIGH)
	GPIO.output(13, GPIO.HIGH)
	GPIO.output(19, GPIO.LOW)

	GPIO.output(26, GPIO.HIGH)
	PWM_A.ChangeDutyCycle(100)
	PWM_B.ChangeDutyCycle(100)

def STOP_ENGINE():
	GPIO.output(26, GPIO.LOW)


camera = PiCamera()
camera.rotation = 180
camera.resolution = (1280, 720)
camera.framerate = 30

def RECORDING():
	video_name = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
	camera.start_recording(str(video_name) + '.h264')
	while GPIO.input(27) == True:
		time.sleep(.001)
	camera.stop_recording()
	CONVERSION(video_name)

def CONVERSION(video_name):
	os.system("MP4Box -add " + video_name + ".h264 " + video_name + ".mp4")
	os.remove(video_name + ".h264")


pixels = neopixel.NeoPixel(board.D18, 12)


ON_OFF = 2


while True:


	button_ON = GPIO.input(17)
	button_OFF = GPIO.input(27)
	button_SHUT_DOWN = GPIO.input(24)


	if button_ON == False:
		ON_OFF = 1

	if button_OFF == False:
		ON_OFF = 0


	if ON_OFF == 1:
		pixels.fill((250, 250, 250))
		START_ENGINE()
		RECORDING()

	if ON_OFF == 0:
		STOP_ENGINE()
		pixels.fill((0, 0, 0))


	if button_SHUT_DOWN == False:
		sleep(5)
		os.system("sudo shutdown -h now")

