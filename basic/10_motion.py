from sense_hat import SenseHat

sense = SenseHat()

### move led with motion
y = 3
x = 3

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
	acceleration = sense.get_accelerometer_raw()
	xAcc = acceleration['x']
	yAcc = acceleration['y']
	zAcc = acceleration['z']

	xAcc=round(xAcc, 0)
	yAcc=round(yAcc, 0)
	zAcc=round(zAcc, 0)

	if xAcc == 1:
		movex(1)
	if xAcc == -1:
		movex(-1)
	if yAcc == 1:
		movey(1)
	if yAcc == -1:
		movey(-1)

	print("x={0}, y={1}, z={2}".format(xAcc, yAcc, zAcc))
