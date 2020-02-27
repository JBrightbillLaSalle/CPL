"""WORK IN PROGRESS

TO DO: Wrap functions into class
Use dictionary instead of pandas"""

import argparse
import os
import pandas as pd
import sys
from sodapy import Socrata
from math import cos, asin, sqrt, isnan
from dotenv import load_dotenv

load_dotenv() # Contains APP_TOKEN as environment variable from .env file
API_BASE: str = 'data.cityofchicago.org'
API_ENDPOINT: str = 'x8fc-8rcq'
APP_TOKEN: str = os.environ['APP_TOKEN']

def connect_api(base:str=API_BASE, endpoint: str=API_ENDPOINT, token: str=APP_TOKEN):
    client = Socrata(base, token)
    result = client.get(endpoint)
    return result

def distance(lat2, lon2):
    """Function to find distance"""
    #lat1, lon1 = row['Lat'], row['Lon']
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * \
        cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a)) #2*R*asin...



df = connect_api(API_BASE, API_ENDPOINT, APP_TOKEN)

df['Distance'] = df.apply(distance, axis=1)
closest = df[df['Distance'] == df['Distance'].min()]

# if len(sys.argv) > 1:
#     point = (float(sys.argv[1]), float(sys.argv[2]))

# # Load and clean data

# libs_json = client.get("x8fc-8rcq")
# libs = json_normalize(libs_json, sep="_")
# libs = libs[['name_', 'address', 'location_latitude', 'location_longitude']]
# libs.rename(columns={'name_':'Name', 'address':'Address', 'location_latitude':'Lat', \
#     'location_longitude':'Lon'}, inplace=True)
# libs['Name'] = libs['Name'].str.upper()
# libs['Lat'] = libs['Lat'].astype(float)
# libs['Lon'] = libs['Lon'].astype(float)

# pop_json = client.get("sw6v-npyj")
# pop = json_normalize(pop_json)
# pop = pop[['location', 'ytd']]
# pop.rename(columns={'location':'Name', 'ytd':'YTD'}, \
#     inplace=True)
# pop['YTD'] = pop['YTD'].astype(float)
# pop['Rank'] = pop['YTD'].rank(ascending=0, method='min')

# df = libs.join(pop.set_index('Name'), on='Name')

# Find closest location using Haversine formula



# library, address, rank = closest.iloc[0]['Name'], closest.iloc[0]['Address'], \
#     closest.iloc[0]['Rank']

# if isnan(rank):
#     rank = 'NA'
# else: 
#     rank = int(rank)

if __name__ == "__main__":
    
    #output = type(APP_TOKEN)
    print(pd.DataFrame.from_records(output))
#     #print(f"{library}   {address}   {rank}")
#     print(libs_json)
