# imports
from sense_hat import SenseHat

# instantiate our sense hat object
sense: SenseHat = SenseHat()

humidity: int | any = sense.get_humidity()
sense.show_message(str(humidity))
