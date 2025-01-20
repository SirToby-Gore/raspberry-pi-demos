from sense_hat import SenseHat

sense: SenseHat = SenseHat()

sense.clear(0,0,0)
     
while True:
	acceleration: dict[str, any] | dict[str, int] = sense.get_accelerometer_raw()
	x: int | any = acceleration['x']
	y: int | any = acceleration['y']
	z: int | any = acceleration['z']

	x = round(x, 0)
	y = round(y, 0)
	z = round(z, 0)

	if x == 0 and y == 0 and z == 1:
		sense.clear(0,255,0)
	else:
		sense.clear(255,0,0)

	print(f"x={x}, y={y}, z={z}")

