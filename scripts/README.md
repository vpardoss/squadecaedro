## Scripts
En este directorio se encuentran los scripts de bash que permiten la automatización de la recolección de datos. Para asegurar la recolección continua de datos, estos scripts están configurados para ejecutarse automáticamente en un servidor mediante tareas de **cron**. El archivo `crontab.txt` documenta la configuración utilizada. El servidor utilizado funciona las 24 horas los 7 días de la semana, corriendo Ubuntu Server 24.04 LTS como sistema operativo.

* **`buses.sh`**: Se encarga de ingresar al entorno virtual de Python en el servidor para posteriormente ejecutar **`extraccion_buses.py`**.
* **`metro.sh`**: Se encarga de ingresar al entorno virtual de Python en el servidor para posteriormente ejecutar **`extraccion_metro.py`**.
* **`hacer_commit.sh`**: Se encarga de añadir **`buses_outputs`** y **`metro_outputs`** al repositorio y posteriormente hacer un commit, con la fecha actual en el comentario de este.
* **`renombrador_archivos.sh`**: Reemplaza el simbolo ":" por "-" en los nombres de todos los archivos de un directorio. Fue usado solo una vez, debido a que Windows no permitía el símbolo ":" en los nombres de los archivos, por lo que se tuvo que renombrar el equivalente a 2 días de datos. (CREADO CON PROMPT DE IA)
* **`crontab.txt`**: Corresponde a la configuración de **cron** utilizada en el servidor.



