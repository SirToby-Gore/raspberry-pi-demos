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

#### Virtual Environment

You will need a virtual environment to install your python packages (supabase, sense-hat & dotenv).

- Make sure you have python3 installed `sudo apt update` then `sudo apt upgrade` then `sudo apt install python3`
- Install pip and venv `sudo apt install python3-pip python3-venv` (you may already have these)
- Create a virtual environment. In the root directory of your project folder run `python -m venv ./venv` do you create a new folder called `venv`. This is your vitrual environment
  - This is essentially creating a new instance of all the necessary python libraries, and allows you to install extra ones. If you're a JS dev, this is basically your `node_modules`
- To activate your virtual environemtn (so you can install things into it and run .py files in it) run `source venv/bin/activate`
- Later when your done, you can run `deactivate` to stop it

Installing our packages that we need for this project

- Run `python -m pip install sense-hat supabase dotenv`
- TODO add about making a requirements file, or even better just using the requirements file in this project
- Alternatively, just run `python -m pip install -r requirements.txt` This will isntall all the packages that are listed in the requirements.txt file
- To create your own in future projects, run `python -m pip freeze > requirements`
  - `pip freeze` on its own lists the packages you have installed, the above snippet puts that content INTO a new requiremnets.txt file

Follow these steps to do this
#### Hardware

1. Attach the SenseHat [link to setting it up](#)
2. Create a copy of `.env.sample` and rename it `.env`. Inside here, put the URL and Key we got from Supabase earlier
2. Open data.py and run it. You should see data start to appear in the database table `readings`

### Client

1. Npm i probably, I'm tired I'll finish this later - Snoop Dogg