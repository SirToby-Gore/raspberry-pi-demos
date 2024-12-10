# imports
from sense_hat import SenseHat


# instansiate our sense hat object
sense = SenseHat()

### move led with joystick
y = 0
x = 0

sense.clear(0,0,0)
sense.set_pixel(x, y, [255,255,255])
def updatematrix():
    global x
    global y
    sense.clear(0,0,0)
    sense.set_pixel(x, y, [255,255,255])

def movex(diff):
    global x
    x += diff
    if x > 7:
        x = 0
    if x < 0:
        x = 7
    updatematrix()
    
def movey(diff):
    global y
    y += diff
    if y > 7:
        y = 0
    if y < 0:
        y = 7
    updatematrix()

while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action)
        if event.action == "pressed":
            if event.direction == "right":
                movex(1)
            if event.direction == "left":
                movex(-1)
            if event.direction == "down":
                movey(1)
            if event.direction == "up":
                movey(-1)

updatematrix()

