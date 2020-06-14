#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO
import os
import signal
import sys
from dotenv import load_dotenv

load_dotenv()

BUTTON_GPIO = int(os.environ['TRIALS_GPIO'])
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)


def button_pressed_callback(channel):
    print("Button pressed!")


print("Waiting for interrupt on GPIO {0}".format(BUTTON_GPIO))

GPIO.add_event_detect(BUTTON_GPIO, GPIO.FALLING,
                      callback=button_pressed_callback, bouncetime=100)

signal.signal(signal.SIGINT, signal_handler)
signal.pause()
