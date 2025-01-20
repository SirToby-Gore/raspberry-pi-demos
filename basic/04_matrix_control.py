# imports
from sense_hat import SenseHat

# instantiate our sense hat object
sense: SenseHat = SenseHat()

### move led with joystick
y: int = 0
x: int = 0

sense.clear(0,0,0)
sense.set_pixel(x, y, [255,255,255])

def update_matrix():
    global x
    global y
    sense.clear(0,0,0)
    sense.set_pixel(x, y, [255,255,255])

def move_x(diff):
    global x

    x += diff

    if x > 7:
        x = 0
    if x < 0:
        x = 7

    update_matrix()
    
def move_y(diff):
    global y

    y += diff

    if y > 7:
        y = 0
    if y < 0:
        y = 7
        
    update_matrix()

while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action)

        events: dict[str, callable] = {
            "right": lambda: move_x(1),
            "left": lambda: move_x(-1),
            "down": lambda: move_y(1),
            "up": lambda: move_y(-1),
        }

        if event.action == "pressed":
            if event.direction in events:
                events[event.direction]()

update_matrix()

