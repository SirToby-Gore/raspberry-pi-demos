# for the collection of data with sensors, and adding that data to the database
import os
from supabase import create_client
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase = create_client(url, key)

temperature = sense.get_temperature() 
pressure = sense.get_pressure()
humidity = sense.get_humidity()

# gather data every 60 seconds
while True:
  data = supabase.table("readings").insert({"temperature": temperature, "pressure":pressure, "humidity":humidity})
  sleep(60)


# example select for testing
#select = supabase.table("readings").select("*").execute()