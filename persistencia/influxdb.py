import pandas as pd
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# Configuración de la conexión a InfluxDB
url = "http://localhost:8086"
token = "16g3qwXL6vHOXKRoS8A234T7IkduQNQx1fNcgkB5T1knlVi4L75J5M6AroFgySaUYUMpvZ-fEGEw7zwoO1VbqQ=="
org = "a"
bucket = "persistencia"

# Crear cliente de InfluxDB
client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Leer datos desde el archivo CSV
file_path = 'T1.csv'
data = pd.read_csv(file_path)

# Insertar datos en InfluxDB con la fecha y hora actuales
for index, row in data.iterrows():
    point = (
        Point("turbine")
        .tag("unit", "turbine1")
        .field("LV ActivePower (kW)", float(row['LV ActivePower (kW)']))
        .field("Wind Speed (m/s)", float(row['Wind Speed (m/s)']))
        .field("Theoretical_Power_Curve (KWh)", float(row['Theoretical_Power_Curve (KWh)']))
        .field("Wind Direction (°)", float(row['Wind Direction (°)']))
        .time(datetime.utcnow(), WritePrecision.MS) # Usar la fecha y hora actuales
    )
    write_api.write(bucket=bucket, org=org, record=point)

# Cerrar el cliente
client.close()