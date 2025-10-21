# Squadecaedro: Análisis de Datos de Transporte Público

EL repositorio del proyecto para la extracción y análisis de datos del sistema de transporte público Red Movilidad. El objetivo principal es recolectar información de buses y metro para su posterior análisis y visualización, siguiendo la propuesta detallada en el archivo PDF del repositorio.

---

## Componentes Principales
Los archivos principales del proyecto corresponden a:

* **`extraccion_buses.py`**: Script de Python encargado de realizar las peticiones a la API y recolectar datos en tiempo real sobre la operación de los buses.
* **`extraccion_metro.py`**: Script de Python similar, enfocado en la recolección de datos sobre el estado de la red de Metro (estado de servicio, estaciones, etc.).
* **`analisis_datos.ipynb`**: Notebook de Jupyter que contiene el Análisis Exploratorio de Datos (EDA). Aquí se limpian, procesan, analizan y visualizan los datos recolectados por los scripts de extracción.
* Las recolecciones de datos se encuentran en los directorios **`buses_outputs`** y **`metro_outputs`**.
---

## Origen de los Datos

La información utilizada en este proyecto se obtiene de la **api-red**, un proyecto desarrollado y mantenido por [Xor.cl](https://xor.cl/).

* **Repositorio de la API:** [https://github.com/xorcl/api-red](https://github.com/xorcl/api-red)

---

## Uso

1.  Revisar los scripts de extracción (`.py`) para entender la recolección de datos.
2.  Ejecutar el notebook `analisis_datos.ipynb` para revisar el análisis completo.
