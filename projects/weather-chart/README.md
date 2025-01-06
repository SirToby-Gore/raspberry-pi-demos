# Weather Chart Project

This project is all the code to run a Pi that collects data on Temperature, Humidity and Pressure, saves it to a PostgreSQL database and displays that data on a client using Vite.

## Components

- Raspberry Pi
- SenseHat

## Installation

### Database

1. Create a Supabase account
2. Create a Supabase Project
3. Run the `CREATE TABLE` SQL statement from `seed.sql`
4. Get the Project URL and your API key from the project settings. You will need these for botht eh Pi setup and the Client setup

### Pi

#### Packages

You will need a virtual environment to install your python packages (supabase, sense-hat & dotenv).

- Make sure you have python3 installed `sudo apt update` then `sudo apt upgrade` then `sudo apt install python3`

- `sudo apt-get install sense-hat`
- `pip install supabase --break-system-packages` - this looks scary, but really, for those familiar with `dangerouslySetHTML`, its about as bad as that.

#### Environment

You will need to give your environment access to your environment variables. you can do this with the below commands, placing the relevant key after the `=`
- `export SUPABASE_URL=`
- `export SUPABASE_ANON_KEY=`

If you close the terminal, you will need to reexport the variables, so have them somewhere handy, but remember giving these to someone is like giving someone your address, a house key & the location of all the valuables in your home... and the ability to just delete your house (that analogy got away from me there).

#### Hardware

1. Attach the SenseHat [link to setting it up](https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat/2)
2. Open data.py and run it. You should see data start to appear in the database table `readings`

### Client

1. Npm i probably, I'm tired I'll finish this later - Snoop Dogg