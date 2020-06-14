#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO
import os
import signal
import sys
from dotenv import load_dotenv

load_dotenv()

BUTTON_GPIO = int(os.environ['TRIALS_BUTTON_GPIO'])
LED_GPIO = int(os.environ['TRIALS_LED_GPIO'])


def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)


def button_callback(channel):
    if GPIO.input(BUTTON_GPIO):
        print("Button pressed!")
        GPIO.output(LED_GPIO, GPIO.LOW)
    else:
        print("Button released!")
        GPIO.output(LED_GPIO, GPIO.HIGH)


GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_GPIO, GPIO.OUT)

GPIO.add_event_detect(BUTTON_GPIO, GPIO.BOTH,
                      callback=button_callback, bouncetime=50)

signal.signal(signal.SIGINT, signal_handler)
signal.pause()
