#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO
import os
import signal
import sys

RINGBELL_GPIO = 16


def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)


def button_callback(channel):
    if GPIO.input(RINGBELL_GPIO):
        print("Someone at the door!")
    else:
        print("Someone stopped ringing!")


GPIO.setmode(GPIO.BCM)
GPIO.setup(RINGBELL_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(RINGBELL_GPIO, GPIO.BOTH,
                      callback=button_callback, bouncetime=50)

signal.signal(signal.SIGINT, signal_handler)
signal.pause()
