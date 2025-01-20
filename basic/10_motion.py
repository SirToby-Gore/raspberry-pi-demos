from sense_hat import SenseHat

sense: SenseHat = SenseHat()

### move led with motion
y: int = 3
x: int = 3

sense.clear(0,0,0)
sense.set_pixel(x, y, [255,255,255])

def update_matrix():
    global x, y
    
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
	acceleration = sense.get_accelerometer_raw()
	xAcc = acceleration['x']
	yAcc = acceleration['y']
	zAcc = acceleration['z']

	xAcc=round(xAcc, 0)
	yAcc=round(yAcc, 0)
	zAcc=round(zAcc, 0)

	if xAcc == 1:
		move_x(1)
	if xAcc == -1:
		move_x(-1)
	if yAcc == 1:
		move_y(1)
	if yAcc == -1:
		move_y(-1)

	print(f"x={xAcc}, y={yAcc}, z={zAcc}")
