# Squadecaedro: Análisis de Datos del Transporte Público de Santiago

Squadecaedro es un proyecto para la extracción y análisis de datos del sistema de transporte público Red Movilidad y del Metro de Santiago. El objetivo principal es recolectar información de buses y metro para su posterior análisis y visualización, siguiendo la propuesta detallada en `squadecaedro_propuesta.ipynb`.

---

## Componentes Principales
Los archivos principales del proyecto corresponden a:

* **`extraccion_buses.py`**: Script de Python encargado de realizar las peticiones a la API y recolectar datos en tiempo real sobre la operación de los buses.
* **`extraccion_metro.py`**: Script de Python similar, enfocado en la recolección de datos sobre el estado de la red de Metro (estado de servicio, estaciones, etc.).
* **`analisis_datos.ipynb`**: Notebook de Jupyter que contiene el Análisis Exploratorio de Datos (EDA). Aquí se limpian, procesan, analizan y visualizan los datos recolectados por los scripts de extracción.
* Las recolecciones de datos se encuentran en los directorios **`buses_outputs`** y **`metro_outputs`**.
---

## Origen de los Datos

* La información de los recorridos de Red son obtienidos de **api-red**, un proyecto desarrollado y mantenido por [Xor.cl](https://github.com/xorcl/api-red).
* La información de los paraderos de buses de Santiago es obtenida de **geojson-Transantiago**, proyecto desarrollado por [JoseDTPM](https://github.com/JoseDTPM/geojson-Transantiago).
#### AQUI DANI AÑADE LO DEL MAPA!!!!!


---

## Sobre la extracción de datos (IMPORTANTE)
La extracción de datos es automatizada, y el proceso está señalado en el README del directorio **`Scripts`**.
* Los datos de los buses de Red se extraen cada 2 horas, de las 6 Hrs a las 22 Hrs.
* Los datos del estado del metro se extraen cada 1 hora, de las 6:30 Hrs a las 22:30 Hrs.
* A las 23 Hrs se realiza un commit automático, que posee como comentario "datos de `{fecha}` añadidos, donde `{fecha}` cambia de forma dinámica (Para más información, ver **`scripts/hacer_commit.sh`**).