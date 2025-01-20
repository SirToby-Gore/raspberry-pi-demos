# imports
from sense_hat import SenseHat

# instantiate our sense hat object
sense: SenseHat = SenseHat()

### hello world scroll
# colours
fore: tuple[int] = (255,91,71)
back: tuple[int] = (0,128,128)

while True:
    sense.show_message("Hello world", scroll_speed = 0.1, text_colour=fore, back_colour=back)
    fore, back = back, fore # swaps back and fore values

