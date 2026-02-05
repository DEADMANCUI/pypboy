#!/usr/bin/python3

import pygame
import argparse
import sys
import settings

#Enable use of cached map via "-c True" command
parser = argparse.ArgumentParser(usage='python %(prog)s -c\nor:\npython %(prog)s -c', prog=sys.argv[0], description='Pip-Boy 3000 MK IV')
parser.add_argument('-c','--cached-map', action="store_true", help="Loads the cached map file stored in map.cache", dest="load_cached", default=False)
parser.add_argument('--version', action='version', version='%(prog)s 0.0.1')
options = parser.parse_args()

try:
    import RPi.GPIO as GPIO
    # GPIO.setmode(GPIO.BCM)
    settings.GPIO_AVAILABLE = True
except Exception as err:
    print("GPIO UNAVAILABLE (%s)" % err)
    settings.GPIO_AVAILABLE = False

if settings.GPIO_AVAILABLE:
    pass

try:
    pygame.mixer.pre_init(44100, -16, 2, 512)
    settings.SOUND_ENABLED = True
except Exception as e:
    settings.SOUND_ENABLED = False

from pypboy.core import Pypboy

if __name__ == "__main__":
    boy = Pypboy('Pip-Boy 3000 MK IV', settings.WIDTH, settings.HEIGHT)
    print("RUN")
    boy.run()