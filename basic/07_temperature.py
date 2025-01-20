# imports
from sense_hat import SenseHat

# instantiate our sense hat object
sense: SenseHat = SenseHat()

# shortcut for get_temperature_from_humidity, alternative is get_temperature_from_pressure
temp: int | any = sense.get_temperature() 
sense.show_message(str(temp))