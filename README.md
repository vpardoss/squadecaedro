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
* **`buses_outputs/`** & **`metro_outputs/`**: Directorios con los logs de datos recolectados en bruto.
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

## 📊 Datos y Metodología ETL

**Fuentes de Datos:**
* **Recorridos y Metro:** [API Red por xorcl](https://github.com/xorcl/api-red) y [API Metro](https://api.xor.cl/red/metro-network).
* **Paraderos:** [geojson-Transantiago por JoseDTPM](https://github.com/JoseDTPM/geojson-Transantiago).
* **Demografía:** [Proyecciones Censo por bastianolea](https://github.com/bastianolea/censo_proyecciones_poblacion).
* **Geografía:** Mapas vectoriales de la BCN.

**Proceso ETL:**
Se automatizó la extracción cada 2 horas (buses) y 1 hora (metro). Posteriormente, se unifican los CSVs diarios, se limpian caracteres erróneos, se cruzan con coordenadas geográficas y se calculan densidades por comuna.

## 🤖 Declaración de Uso de IA y Referencias
* **Inteligencia Artificial:** Se utilizó IA Generativa para apoyar la creación del script `renombrador_archivos.sh` (manipulación de strings en Bash), solo fue utilizado una vez (más información en README de la carpeta **`scripts/`**.
* **Referencias Bibliográficas:** Disponibles detalladamente en `analisis_datos.ipynb`.