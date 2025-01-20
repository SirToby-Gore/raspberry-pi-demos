# imports
from sense_hat import SenseHat

# instantiate our sense hat object
sense: SenseHat = SenseHat()

pressure: int | any = sense.get_pressure()
sense.show_message(str(pressure))