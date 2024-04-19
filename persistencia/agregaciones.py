from influxdb_client import InfluxDBClient
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# Configuración de la conexión a InfluxDB
url = "http://localhost:8086"
token = "16g3qwXL6vHOXKRoS8A234T7IkduQNQx1fNcgkB5T1knlVi4L75J5M6AroFgySaUYUMpvZ-fEGEw7zwoO1VbqQ=="
org = "a"
bucket = "persistencia"

# Crear cliente de InfluxDB
client = InfluxDBClient(url=url, token=token, org=org)
query_api = client.query_api()

# Consultas en Flux para diferentes agregaciones
queries = {
    "Media de Potencia Activa": f'''
        from(bucket: "{bucket}")
        |> range(start: -1d)
        |> filter(fn: (r) => r["_measurement"] == "turbine")
        |> filter(fn: (r) => r["_field"] == "LV ActivePower (kW)")
        |> mean()
    ''',
    "Máximo de Velocidad del Viento": f'''
        from(bucket: "{bucket}")
        |> range(start: -1d)
        |> filter(fn: (r) => r["_measurement"] == "turbine")
        |> filter(fn: (r) => r["_field"] == "Wind Speed (m/s)")
        |> max()
    ''',
    "Mínimo de Velocidad del Viento": f'''
        from(bucket: "{bucket}")
        |> range(start: -1d)
        |> filter(fn: (r) => r["_measurement"] == "turbine")
        |> filter(fn: (r) => r["_field"] == "Wind Speed (m/s)")
        |> min()
    ''', # Añade una coma aquí
    "Suma de Potencia Teórica": f'''
        from(bucket: "{bucket}")
        |> range(start: -1d)
        |> filter(fn: (r) => r["_measurement"] == "turbine")
        |> filter(fn: (r) => r["_field"] == "Theoretical_Power_Curve (KWh)")
        |> sum()
    '''
}

# Preparar los datos para el histograma
num_sectors = 16
sector_angles = np.linspace(0, 360, num_sectors + 1)
sector_counts, _ = np.histogram(data['direction'], bins=sector_angles)

# Crear la rosa de los vientos
ax = plt.subplot(111, polar=True)
bars = ax.bar(np.deg2rad(sector_angles[:-1]), sector_counts, width=np.deg2rad(360/num_sectors), bottom=0.0, color='b', edgecolor='black')

# Configurar la gráfica
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
plt.title('Rosa de los Vientos')

# Especifica la ruta y el nombre del archivo donde guardarás la imagen
file_path = '/home/juan/persistencia/wind_rose.png'

# Guardar la figura
plt.savefig(file_path)

# Verificar si el archivo fue creado
if os.path.exists(file_path):
    print("La imagen se ha guardado correctamente.")
else:
    print("Error al guardar la imagen.")

plt.close() # Cierra la figura para liberar memoria

# Ejecutar consultas y mostrar resultados
for desc, query in queries.items():
    result = query_api.query(org=org, query=query)
    results = []
    for table in result:
        for record in table.records:
            results.append(record.get_value())
    print(f"{desc}: {results}")

# Cerrar el cliente
client.close()