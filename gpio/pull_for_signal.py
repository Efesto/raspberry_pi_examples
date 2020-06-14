#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO
import os
from dotenv import load_dotenv

load_dotenv()

BUTTON_GPIO = int(os.environ['TRIALS_GPIO'])
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
pressed = False

print("Waiting for input on GPIO {0}".format(BUTTON_GPIO))

while True:
    # button is pressed when pin is LOW
    if not GPIO.input(BUTTON_GPIO):
        if not pressed:
            print("Button pressed!")
            pressed = True
    # button not pressed (or released)
    else:
        pressed = False
    time.sleep(0.1)
