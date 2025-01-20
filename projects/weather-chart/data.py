# for the collection of data with sensors, and adding that data to the database
import os
from supabase import create_client
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_ANON_KEY")

supabase: any = create_client(url, key)

# gather data every 60 seconds
while True:
    temperature: int | any = sense.get_temperature() 
    pressure: int | any = sense.get_pressure()
    humidity: int | any = sense.get_humidity()
    print(temperature)
    print(pressure)
    print(humidity)
    data: any = supabase.table("readings").insert({"temperature": temperature, "pressure":pressure, "humidity":humidity}).execute()
    print("Added to db")
    sleep(60) # waits for 1 min, 60 seconds


# example select for testing
#select = supabase.table("readings").select("*").execute()