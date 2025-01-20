# https://github.com/planetschool/sensehat-balance-game
#### Tea, Lucien ####

from sense_hat import SenseHat
from datetime import datetime
from time import sleep

# logging settings

FILENAME: str = "Lucien,Tea"
WRITE_FREQUENCY: int = 5

# functions
def revise_orientation(original_angle: int) -> int:
	global sense

	o: dict[str, any] | dict[str, int] = sense.get_orientation()
	name: int = original_angle
	x: int = int() # early init

	if original_angle == "roll":
		original_angle: int | any = o["roll"]
		if original_angle >= 320 and original_angle < 330:
			x = 0
		elif original_angle >= 330 and original_angle < 340:
			x = 1  
		elif original_angle >= 340 and original_angle < 350:
			x = 2
		elif original_angle >= 350:
			x = 3
		elif original_angle <= 10:
			x = 4
		elif original_angle <= 20:
			x = 5
		elif original_angle <= 30:
			x = 6
		elif original_angle <= 40:
			x = 7
		else:
			for x in range(0,8):
				for y in range(0,8):
					sense.set_pixel(x, y, 0, 0, 0)
	
	elif original_angle == "pitch":
		original_angle = o["pitch"]

		# for roll, 0 = 330 7 = 30
		# for pitch, 0 = 30 7 = 330
		if original_angle >= 320 and original_angle < 330:
			x = 7
		elif original_angle >= 330 and original_angle < 340:
			x = 6  
		elif original_angle >= 340 and original_angle < 350:
			x = 5
		elif original_angle >= 350:
			x = 4
		elif original_angle <= 10:
			x = 3
		elif original_angle <= 20:
			x = 2
		elif original_angle <= 30:
			x = 1
		elif original_angle <= 40:
			x = 0
		else:
			for x in range(0,8):
				for y in range(0,8): sense.set_pixel(x, y, 0, 0, 0)
	
	print(f"{name} is {x}")	

	return x
	
def light_game(pitch, roll):
	# example using (x, y, r, g, b)
	red: tuple[int] = (255, 0, 0)
	green: tuple[int] = (0, 255, 0)
	blue: tuple[int] = (0, 0, 255)
	sense.set_pixel(pitch, roll, green)
	# sense.set_pixel(0, 7, 255, 255, 255)
	# sense.set_pixel(7, 0, 0, 0, 255)
	# sense.set_pixel(7, 7, 244, , 255)
	'''
	red = (255, 0, 0)
	green = (0, 255, 0)
	blue = (0, 0, 255)

	#example using (x, y, pixel)
	sense.set_pixel(0, 0, red)
	sense.set_pixel(0, 0, green)
	sense.set_pixel(0, 0, blue)
	'''

def log_data() -> None:
	global sense_data, batch_data
	
	output_string = ",".join([str(value) for value in sense_data])
	batch_data.append(output_string)

def file_setup(filename: str):
	header: list[str] = [
		"temp_h",
		"temp_p",
		"humidity",
		"pressure",
		"pitch",
		"roll",
		"yaw",
		"mag_x",
		"mag_y",
		"mag_z",
		"accel_x",
		"accel_y",
		"accel_z",
		"gyro_x",
		"gyro_)y",
		"gyro_z",
		"timestamp"
	]

def get_sense_data() -> list[int | any | datetime]:
	global sense

	sense_data: list[int | any | datetime] = []
	 
	sense_data.append(sense.get_temperature_from_humidity())
	sense_data.append(sense.get_temperature_from_pressure())
	sense_data.append(sense.get_humidity())
	sense_data.append(sense.get_pressure())

	o: dict[str, any] | dict[str, int] = sense.get_orientation()
	yaw: int | any = o["yaw"]
	pitch: int | any = o["pitch"]
	roll: int | any = o["roll"]
	sense_data.extend([pitch,roll,yaw])

	mag: dict[str, any] | dict[str, int] = sense.get_compass_raw()
	mag_x: int | any = mag["x"]
	mag_y: int | any = mag["y"]
	mag_z: int | any = mag["z"]
	sense_data.extend([mag_x,mag_y,mag_z])

	acc: dict[str, any] | dict[str, int] = sense.get_accelerometer_raw()
	x: int | any = acc["x"]
	y: int | any = acc["y"]
	z: int | any = acc["z"]
	sense_data.extend([x,y,z])

	gyro: dict[str, any] | dict[str, int] = sense.get_gyroscope_raw()
	gyro_x: int | any = gyro["x"]
	gyro_y: int | any = gyro["y"] 
	gyro_z: int | any = gyro["z"]
	sense_data.extend([gyro_x,gyro_y,gyro_z])

	sense_data.append(datetime.now())

	return sense_data


### Main Program ###
def main() -> None:
	global sense

	sense: SenseHat = SenseHat()
	
	# while True:
	# 	o = sense.get_orientation()
	# 	pitch = o["pitch"]
	# 	roll = o["roll"]
	# 	print("Roll is %s and pitch is %s" % (roll, pitch))

	pitch: str = "pitch"
	roll: str = "roll"

	for x in range(0,8):
		for y in range(0,8):
			sense.set_pixel(x, y, 0, 0, 0)
			
	while True:
		a: int = x
		b: int = y
		x: int = revise_orientation(pitch)
		y: int = revise_orientation(roll)

		light_game(x, y)
		
		if b != y and a != x:
			sense.set_pixel(a, b, 0, 0, 0)
		elif a != x:
			sense.set_pixel(a, y, 0, 0, 0)
			print("Pitch changed!")
		elif b != y:
			sense.set_pixel(x, b, 0, 0, 0)
			print("Roll changed!")
		print(f"A is {a} and X is {x}")
		
	# batch_data = []

	# if FILENAME == "Lucien,Tea":
	# 	filename = "" +str(datetime.now())+".csv"	
	# else:
	# 	filename = FILENAME+"-"+str(datetime.now())+".csv"

	# file_setup(filename)

	# while True:
	# 	sense_data = get_sense_data()
	# 	log_data() 
		

	# 	if len(batch_data) >= WRITE_FREQUENCY:
	# 		print("Writing to file...")
	# 		with open(filename, "a") as f:
	# 			for line in batch_data:
	# 				f.write(line + "\n")
	# 			batch_data = []

if __name__ == "__main__":
	main()