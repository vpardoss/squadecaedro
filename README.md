# Squadecaedro: Análisis de Datos del Transporte Público de Santiago

Squadecaedro es un proyecto para la extracción y análisis de datos del sistema de transporte público Red Movilidad y del Metro de Santiago. El objetivo principal es recolectar información de buses y metro para su posterior análisis y visualización, siguiendo la propuesta detallada en `squadecaedro_propuesta.ipynb`.

---

## Componentes Principales
Los archivos principales del proyecto corresponden a:

* **`analisis_datos.ipynb`**: Notebook de Jupyter que contiene el Análisis Exploratorio de Datos (EDA). Aquí se limpian, procesan, analizan y visualizan los datos recolectados por los scripts de extracción.
* **`squadecaedro_propuesta.ipynb`**: Notebook de Jupyter que contiene el resumen del proyecto hasta la fecha.
* **`extraccion_buses.py`**: Script de Python encargado de realizar las peticiones a la API y recolectar datos en tiempo real sobre la operación de los buses.
* **`extraccion_metro.py`**: Script de Python similar, enfocado en la recolección de datos sobre el estado de la red de Metro (estado de servicio, estaciones, etc.).
* Las recolecciones de datos se encuentran en los directorios **`buses_outputs`** y **`metro_outputs`**.
---

## Origen de los Datos

* La información de los recorridos de Red es obtenida de **api-red**, un proyecto desarrollado por **xorcl** en [GitHub](https://github.com/xorcl/api-red).
* La información de los paraderos de buses de Santiago es obtenida de **geojson-Transantiago**, proyecto desarrollado por **JoseDTPM** en [GitHub](https://github.com/JoseDTPM/geojson-Transantiago).
* Los datos de las proyecciones de población del Censo fueron obtenidos de **censo_proyecciones_poblacion**, proyecto desarrollado por **bastianolea** en [GitHub](https://github.com/bastianolea/censo_proyecciones_poblacion).
* Los mapas vectoriales de la RM fueron obtenidos de la [colección de mapas vectoriales de la BCN](https://www.bcn.cl/siit/mapas_vectoriales).


---
## Extracción de datos

### Scripts
En el directorio **`Scripts`** se encuentran los scripts de bash que permiten la automatización de la recolección de datos. Para asegurar la recolección continua de datos, estos scripts están configurados para ejecutarse automáticamente en un servidor mediante tareas de **cron**. El archivo `crontab.txt` documenta la configuración utilizada. El servidor utilizado funciona las 24 horas los 7 días de la semana, corriendo Ubuntu Server 24.04 LTS como sistema operativo.

* **`buses.sh`**: Se encarga de ingresar al entorno virtual de Python en el servidor para posteriormente ejecutar **`extraccion_buses.py`**.
* **`metro.sh`**: Se encarga de ingresar al entorno virtual de Python en el servidor para posteriormente ejecutar **`extraccion_metro.py`**.
* **`hacer_commit.sh`**: Se encarga de añadir **`buses_outputs`** y **`metro_outputs`** al repositorio y posteriormente hacer un commit, con la fecha actual en el comentario de este.
* **`renombrador_archivos.sh`**: Reemplaza el simbolo ":" por "-" en los nombres de todos los archivos de un directorio. Fue usado solo una vez, debido a que Windows no permitía el símbolo ":" en los nombres de los archivos, por lo que se tuvo que renombrar el equivalente a 2 días de datos. (CREADO CON PROMPT DE IA)
* **`crontab.txt`**: Corresponde a la configuración de **cron** utilizada en el servidor.



### Sobre la extracción de datos (IMPORTANTE)
La extracción de datos es automatizada, y el proceso está señalado en el README del directorio **`Scripts`**.
* Los datos de los buses de Red se extraen cada 2 horas, de las 6 Hrs a las 22 Hrs.
* Los datos del estado del metro se extraen cada 1 hora, de las 6:30 Hrs a las 22:30 Hrs.
* A las 23 Hrs se realiza un commit automático, que posee como comentario "datos de `{fecha}` añadidos", donde `{fecha}` cambia de forma dinámica (Para más información, ver **`scripts/hacer_commit.sh`**).