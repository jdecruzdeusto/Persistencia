
# Reto: Procesamiento de Datos

Introducción a FastApi, pydantic y OAuth

## Descripción:

- Explorar el siguiente dataset: https://www.kaggle.com/datasets/berkerisen/wind-turbine-scada-dataset
  
- En base a este caso de uso elegir un modelo de base de datos apropiado para gestionar una turbina de viento.
  
- Generar una aplicación que lea el dataset y lo inserte en la base de datos (actualizando las marcas de tiempo).

- Calcula diferentes tipos de agregaciones como demostración.
  
- Extra: Demostrar mediante una visualización la inserción de datos correcta y argumentar la elección de la base de datos.

## Estructura 🏗️

![image](https://github.com/jdecruzdeusto/Persistencia/assets/125390240/bba31325-ae50-48cf-9a11-e5eed1fe819d)

## Ejecución 🚀

0. REQUERIMIENTOS

Instalar los paquetes necesarios:
```bash
pip install influxdb-client
pip install matplotlib
```

1. Ejecutar el archivo influxdb.py
```bash
python3 influxdb.py
```

2. Ejecutar agregaciones.py:
```bash
python3 agregaciones.py
```
3. Abrir InfluxDB utilizando la siguiente URL:
```url
http://localhost:8086
```

## Pasos seguidos para realizar el reto 🚶

1. Leer y entender de qué era el csv y seleccionar la tecnología adecuada
   
2. Leer y aplicar la documentación de InfluxDB
   
3. Crear el archivo principal (influxdb.py) para que inserte los datos
   
4. Crear las agregaciones buscando cómo hacer las queries de InfluxDB
   
5. Crear un Dashboard para ver los datos mejor organizados

## Posibles vías de mejora 📈
- Implementar otras formas de visualizar los datos

- Meter más datos y de otras fuentes

- Realizar agregaciones más complejas para analizar y explotar los datos


## Alternativas posibles 🔜
- Otras DBs temporales:

  - Prometheus

- DBs noSQL:
  
  - MongoDB

- Utilizar otros lenguajes que sean más óptimos energéticamente

  - C


## Problemas / Retos encontrados ❗
- Fallo crítico en el ordenador

- Poca familiaridad con InfluxDB

- Comprensión inicial del reto

