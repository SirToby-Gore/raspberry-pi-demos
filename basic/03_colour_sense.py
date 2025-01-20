# imports
from sense_hat import SenseHat
from time import sleep

# instantiate our sense hat object
sense: SenseHat = SenseHat()
sense.color.gain = 64 # sensitivity of sensor - 1,4,16 or 64
sense.color.integration_cycles = 64 # time between measurements - 1 cycle = 2.4 milliseconds can be anything from 1-256

while True:
    sleep(2 * sense.color.integration_time)
    red, green, blue, clear = sense.colour.colour # readings are scaled to 0-256
    sense.clear(
        min(red, 255),
        min(green, 255),
        min(blue,255)
    ) # min because if its so bright, 256 is an invalid rgb value
    print(red, green, blue)
