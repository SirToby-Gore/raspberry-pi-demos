# imports
from sense_hat import SenseHat

# instansiate our sense hat object
sense = SenseHat()

### hello world scroll
# colours
fore = [255,91,71]
back = [0,128,128]

while True:
    sense.show_message("Hello world", scroll_speed = 0.1, text_colour=fore, back_colour=back)
    temp = back
    back = fore
    fore = temp

