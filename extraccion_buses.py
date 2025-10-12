# Creamos un dataframe que tenga todos los ID de paraderos de Santiago usando
# https://raw.githubusercontent.com/JoseDTPM/geojson-Transantiago/refs/heads/main/Paraderos-Santiago-Chile.geojsonl.json

import pandas as pd
import requests
import time
from datetime import datetime
from alive_progress import alive_bar

file = 'data/Paraderos-Santiago-Chile.geojsonl.json'
df = pd.read_json(file, lines=True)
properties_df = pd.json_normalize(df['properties'])

# Seleccionamos la columna que corresponde al ID de los paraderos.
stops_df = properties_df[['SIMT', 'X', 'Y']]
stops_df_clean = pd.DataFrame()
stops_df_clean['SIMT'] = stops_df['SIMT'].unique()
stops_df_500 = stops_df.sample(n = 500).reset_index()
print(f"Comenzando extracción:")
stops_df_500
'''
timeanddate = datetime.now()

timeanddate = timeanddate.strftime("%d-%m-%Y-%H:%M:%S")

def bus_routes(stop):
    all_routes_data = []
    total_stops = len(stop)
    i = 0
    with alive_bar(total_stops) as bar:
        for code in stops_df['SIMT']:
            print(f"Paradero actual: {code}")
            url = f"https://api.xor.cl/red/bus-stop/{code}"
            response = requests.get(url)
            data = response.json()
            
            for service in data.get('services', []):
                    for bus in service.get('buses', []):
                        all_routes_data.append({
                            'bus_stop_code': code,
                            'route_id': service.get('id'),
                            'bus_id': bus.get('id'),
                            'meters_distance': bus.get('meters_distance'),
                            'min_arrival_time': bus.get('min_arrival_time'),
                            'max_arrival_time': bus.get('max_arrival_time')
                })
            bar()
    bus_routes = pd.DataFrame(all_routes_data)                
    final_df = pd.merge(
    bus_routes,
    stops_df,
    left_on='bus_stop_code',
    right_on='SIMT',
    how='left'
    )

    final_df = final_df.drop(columns=['SIMT'])
    return final_df

final_bus_df = bus_routes(stops_df_500)
final_bus_df

final_bus_df.to_csv(f"datos_{timeanddate}.csv", index=False)
print("CSV creado")
'''