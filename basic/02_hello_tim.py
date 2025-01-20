# imports
from sense_hat import SenseHat
from time import sleep
from random import randint

# instantiate our sense hat object
sense: SenseHat = SenseHat()

### show Tim
rand_col_1: list[int] = [randint(0,255),randint(0,255),randint(0,255)]
rand_col_2: list[int] = [randint(0,255),randint(0,255),randint(0,255)]
rand_col_3: list[int] = [randint(0,255),randint(0,255),randint(0,255)]

sense.show_letter("T", rand_col_1)
sleep(1)
sense.show_letter("i", rand_col_2)
sleep(1)
sense.show_letter("m", rand_col_3)
sleep(1)

sense.clear(0,0,0)


