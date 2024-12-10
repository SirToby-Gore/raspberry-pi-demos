# imports
from sense_hat import SenseHat

# instansiate our sense hat object
sense = SenseHat()

humidity = sense.get_humidity()
sense.show_message(str(humidity))
