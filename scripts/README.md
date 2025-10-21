## Scripts
En este directorio se encuentran los scripts de bash que permiten la automatización de la recolección de datos. Para asegurar la recolección continua de datos, estos scripts están configurados para ejecutarse automáticamente en un servidor mediante tareas de **cron**. El archivo `crontab.txt` documenta la configuración utilizada.

* **`buses.sh`**: Se encarga de ingresar al entorno virtual de Python para posteriormente ejecutar **`extraccion_buses.py`**.
* **`metro.sh`**: Se encarga de ingresar al entorno virtual de Python para posteriormente ejecutar **`extraccion_metro.py`**.
* **`hacer_commit.sh`**: Se encarga de añadir **`buses_outputs`** y **`metro_outputs`** al repositorio y posteriormente hacer un commit, con la fecha actual en el comentario de este.
* **`renombrador_archivos.sh`**: Reemplaza el simbolo ":" por "-" en los nombres de todos los archivos de un directorio. Fue usado solo una vez, debido a que Windows no permitía el símbolo ":" en los nombres de los archivos. (CREADO CON PROMPT DE IA)
* **`crontab.txt`**: Corresponde a la configuración de **cron** utilizada en el servidor.



