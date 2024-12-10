# imports
from sense_hat import SenseHat
from time import sleep
from random import randint

# instansiate our sense hat object
sense = SenseHat()



### show Tim
randcol1 = [randint(0,255),randint(0,255),randint(0,255)]
randcol2 = [randint(0,255),randint(0,255),randint(0,255)]
randcol3 = [randint(0,255),randint(0,255),randint(0,255)]

sense.show_letter("T", randcol1)
sleep(1)
sense.show_letter("i", randcol2)
sleep(1)
sense.show_letter("m", randcol3)
sleep(1)
sense.clear(0,0,0)


