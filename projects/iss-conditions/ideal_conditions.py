# from the raspberry pi demos
from sense_hat import SenseHat
sense: SenseHat = SenseHat()

# define the colours red and green
red: tuple[int] = (255, 0, 0)
green: tuple[int] = (0, 255, 0)

while True:

  # take readings from all three sensors
  t: int | any = sense.get_temperature()
  p: int | any = sense.get_pressure()
  h: int | any = sense.get_humidity()

  # round the values to one decimal place
  t = round(t, 1)
  p = round(p, 1)
  h = round(h, 1)
  
  # create the message
  message: str = f"Temperature: {t} Pressure: {p} Humidity: {h}"
  
  if t > 18.3 and t < 26.7:
    bg: tuple[int] = green
  else:
    bg: tuple[int] = red
  
  # display the scrolling message
  sense.show_message(message, scroll_speed=0.05, back_colour=bg)