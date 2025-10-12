import pandas as pd
import requests
import time
from datetime import datetime
from alive_progress import alive_bar

def get_metro_data():
    url = "https://api.xor.cl/red/metro-network"
    all_stations_data = []

    response = requests.get(url)
    lines_data = response.json()

    lines_list = lines_data.get("lines", [])
    with alive_bar(len(lines_list)) as bar:
        for line in lines_list:
            line_id = line.get("id")
            
            stations = line.get("stations", [])
            
            for station in stations:
                current_datetime = datetime.now()
                all_stations_data.append({
                    "line_id": line_id,
                    "station_id": station.get("id"),
                    "name": station.get("name"),
                    "status_code": station.get("status"),
                    "status_description": station.get("description"),
                    "date": current_datetime
                })
        bar()
    
    return pd.DataFrame(all_stations_data)

timeanddate = datetime.now()
timeanddate = timeanddate.strftime("%d-%m-%Y-%H:%M")
    
metro_df = get_metro_data()

metro_df.to_csv(f"metro_{timeanddate}.csv", index=False)
print("CSV creado.")