# Weather Chart Project

This project is all the code to run a Pi that collects data on Temperature, Humidity and Pressure, saves it to a PostgreSQL database and displays that data on a client using Vite.

## Components

- Raspberry Pi
- SenseHat

## Installation

### Database

1. Create a Supabase account
2. Create a Supabase Project
3. Run the `CREATE TABLE` SQL statement from 
4. Get the Project URL and your API key from the project settings. You will need these for botht eh Pi setup and the Client setup

### Pi

1. Attach the SenseHat [link to setting it up](#)
2. Create a copy of `.env.sample` and rename it `.env`. Inside here, put the URL and Key we got from Supabase earlier
2. Open data.py and run it. You should see data start to appear in the database table `readings`

### Client

1. Npm i probably, I'm tired I'll finish this later - Snoop Dogg