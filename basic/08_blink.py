# imports
from sense_hat import SenseHat
from time import sleep
from random import randint

# instantiate our sense hat object
sense: SenseHat = SenseHat()

while True:
    sense.clear(randint(0,255),randint(0,255),randint(0,255))
    sleep(1)
    sense.clear(0,0,0)
    sleep(1)