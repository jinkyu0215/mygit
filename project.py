import pygame.mixer
import RPi.GPIO as GPIO
import time
import serial
from Adafruit_CharLCD import Adafruit_CharLCD
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

lcd= Adafruit_CharLCD()
lcd.begin(16,1)

pygame.mixer.init(48000,-16,1,1024)
sound = pygame.mixer.Sound("match5.wav")
ChannelA = pygame.mixer.Channel(1)

port="/dev/ttyUSB0"
serialFromAduino=serial.Serial(port, 9600)
serialFromAduino.flushInput()


while True:
	GPIO.output(21,GPIO.LOW)
	GPIO.output(19,GPIO.LOW)
	GPIO.output(16,GPIO.LOW)


	input_s = serialFromAduino.readline()
	lcd.clear()
	lcd.message(input_s)

	input = int(input_s)
	print(input)
	if(0 <=input & input <=69):
		GPIO.output(21,GPIO.HIGH) 	
			
	if(70 <=input & input <=109):
		GPIO.output(19,GPIO.HIGH)
		
	if(110 <=input & input <=200):
		GPIO.output(16,GPIO.HIGH)
	inputValue = GPIO.input(13)
	if(inputValue==True):
		print("OK")
	if(inputValue==False):
		if(120<=input & input <=200):
			ChannelA.play(sound)
			print("DIE")	
	time.sleep(5)



