# imports
from sense_hat import SenseHat
from time import sleep
from random import randint

# instantiate our sense hat object
sense: SenseHat = SenseHat()

while True:
    matrix: list[tuple[int]] = []
    for x in range(64):
        rand_col = (randint(0, 255), randint(0, 255), randint(0, 255))
        matrix.append(rand_col)

    sense.set_pixels(matrix)
    sleep(1)
    sense.clear(0,0,0)
    sleep(1)
