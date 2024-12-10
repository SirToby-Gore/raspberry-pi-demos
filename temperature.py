# imports
from sense_hat import SenseHat

# instansiate our sense hat object
sense = SenseHat()

# shortcut for get_temperature_from_humidity, alternative is get_temperature_from_pressure
temp = sense.get_temperature() 
sense.show_message(str(temp))