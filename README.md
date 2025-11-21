# Squadecaedro: Análisis de Datos del Transporte Público de Santiago

Proyecto de Ciencia de Datos enfocado en la extracción, procesamiento y análisis de la operación de buses (Red Movilidad) y Metro de Santiago para detectar patrones de ineficiencia, retrasos y correlaciones con la densidad demográfica.

## 👥 Equipo y Roles
* **Carolina Lobos**: [Rol: ETL y Análisis Exploratorio]
* **Daniela Espinoza**: [Rol: Análisis Exploratorio y Visualización]
* **Vicente Pardo**: [Rol: ETL y Scripts de extracción]

## 📂 Estructura del Repositorio
El proyecto sigue una jerarquía ordenada para facilitar la reproducibilidad:

* **`data/`**: Contiene los datos crudos de paraderos, censo y mapas vectoriales.
* **`notebooks/`**:
    * `squadecaedro_entrega.ipynb`: Notebook principal del proyecto. Contiene los resultados del proyecto.
    * `unificacion_datos.ipynb`: Script de ETL para limpieza y fusión de CSVs.
    * `analisis_datos.ipynb`: EDA principal, visualizaciones y respuesta a preguntas de investigación.
    * `extraccion_datos.ipynb`: Notebook demostrativo del proceso de consulta a APIs.
* **`scripts/`**: Scripts Python (`.py`) y Bash (`.sh`) para la automatización de extracción en servidor (Cron).
* **`buses_outputs/`** & **`metro_outputs/`**: Directorios con los datos recolectados en bruto.
* **`csv_unificado_*/`**: Resultados del proceso de ETL listos para análisis.

## ⚙️ Instrucciones de Ejecución

1.  **Instalación de dependencias:**
    Asegúrese de tener las librerías necesarias (pandas, matplotlib, geopandas, requests).
2.  **Recolección de Datos (Opcional):**
    Los scripts en `scripts/` están configurados para correr automáticamente (Crontab) en un servidor Linux (Para más información, ver README de **`scripts/`**. Para una prueba manual, ejecute `extraccion_datos.ipynb`.
3.  **Procesamiento (ETL):**
    Ejecute **`unificacion_datos.ipynb`**. Este notebook toma los archivos crudos de las carpetas `_outputs`, limpia los formatos y genera los archivos unificados en `csv_unificado_buses/` y `csv_unificado_metro/`.
4.  **Análisis:**
    Ejecute **`analisis_datos.ipynb`** para generar las visualizaciones y métricas finales basadas en los datos unificados.

---

## 📚 Origen de los Datos y Referencias

### Fuentes de Datos

* La información de los **recorridos de Red** es obtenida de **api-red**, un proyecto desarrollado por **xorcl** en [GitHub](https://github.com/xorcl/api-red).
* La información de los **paraderos de buses** de Santiago es obtenida de **geojson-Transantiago**, proyecto desarrollado por **JoseDTPM** en [GitHub](https://github.com/JoseDTPM/geojson-Transantiago).
* Los datos de las **proyecciones de población del Censo** fueron obtenidos de **censo_proyecciones_poblacion**, proyecto desarrollado por **bastianolea** en [GitHub](https://github.com/bastianolea/censo_proyecciones_poblacion).
* Los **mapas vectoriales** de la RM fueron obtenidos de la [colección de mapas vectoriales de la BCN](https://www.bcn.cl/siit/mapas_vectoriales).

### Contexto y Motivación

* [Proyecciones de Población - Censo 2024](https://censo2024.ine.gob.cl/)
* [Análisis de Fallas del Metro y Planes de Mejora](https://www.latercera.com/pulso/noticia/domingo-las-fallas-del-metro-sus-cifras-sus-razones-y-sus-planes-de-mejora/)
* [Estudio de la Facultad de Ingeniería y Ciencias Aplicadas de la Universidad de los Andes (2023)](https://share.google/QhiIblNkQYCp1jG5e)
* [Matrices de Viaje - DTPM](https://www.dtpm.cl/index.php/documentos/matrices-de-viaje)
* [Definición de "Urbanización" (RAE)](https://dle.rae.es/urbanizaci%C3%B3n)
* [Definición de "Urbanizar" (RAE)](https://dle.rae.es/urbanizar?m=form)
* [Datos sobre Urbanización a Nivel Mundial (Our World in Data)](https://ourworldindata.org/urbanization)

## 💻 Extracción de datos

### Scripts
En el directorio **`Scripts`** se encuentran los scripts de bash que permiten la automatización de la recolección de datos. Para asegurar la recolección continua de datos, estos scripts están configurados para ejecutarse automáticamente en un servidor mediante tareas de **cron**. El archivo `crontab.txt` documenta la configuración utilizada. El servidor utilizado funciona las 24 horas los 7 días de la semana, corriendo Ubuntu Server 24.04 LTS como sistema operativo.

* **`extraccion_buses.sh`**: Se encarga de extraer los datos de buses.
* **`buses.sh`**: Se encarga de extraer los datos de metro.
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

---

## 🤖 Declaración de Uso de IA
* **Inteligencia Artificial:** Como ya fue mencionado, se utilizó IA para la creación del script `renombrador_archivos.sh` (manipulación de strings en Bash), solo fue utilizado una vez (más información en README de la carpeta **`scripts/`**).
