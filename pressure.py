# imports
from sense_hat import SenseHat

# instansiate our sense hat object
sense = SenseHat()

pressure = sense.get_pressure()
sense.show_message(str(pressure))