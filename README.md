# BitSocial

Antes de desarrollar, leer esto:

En el mundo del desarrollo colaborativo, para evitar problemas con las librerías y módulos externos debemos seguir algunas pautas para que todos tengamos la misma versión de dichas librerías y módulos. Por eso les voy a dejar una serie de pasos que tiene que hacer antes de ponerse a codear para que todo nos funcione a todos.

1. Una vez instalado python, abierto VSC en la carpeta donde vamos a tener nuestro repositorio local, y descargado el repositorio desde Github. Debemos abrir una terminal y posicionarnos en la carpeta que se llama antisocial que adentro tiene dos carpetas scripts y src. En la terminal debemos ejecutar el siguiente comando:

```
pip install virtualenv

```

Esto instala a nivel global (en toda la computadora), una librería que sirve para encapsular nuestros proyectos y evitar conflictos con otras librerías de otros proyectos.

2. Luego, crea el entorno virtual utilizando virtualenv. Puedes elegir un nombre para tu entorno (por ejemplo, venv):

```
virtualenv venv
```

Esto creará una carpeta llamada myenv en el directorio actual, que contendrá el entorno virtual.

Los entornos virtuales hacen que las librerías que instalemos, solo funcionen en este proyecto, por lo cual reduce la posibilidad de errores y facilitará que todos tengamos la posibilidad de instalar las mismas librerías con las mismas versiones.

3. Activar el entorno virtual:

Después de crear el entorno virtual, debes activarlo. Esto establecerá las variables de entorno necesarias para que Python y pip funcionen dentro del entorno virtual. En la Terminal, ejecuta:

```
venv\Scripts\activate
```

Una vez que está activo el entorno virtual te va a mostrar los antes de arrancar la linea en la terminal "(venv)". Sin las comillas.

4. Instalar paquetes y crear requirements.txt:

```
pip install nombre-del-paquete
```

Luego, crea un archivo requirements.txt para guardar los paquetes y sus versiones:

```
pip freeze > requirements.txt

```

5. Cerrar el proyecto y cargar los cambios en GitHub:

Cuando hayas terminado de trabajar, sigue estos pasos para cargar los cambios en tu repositorio de GitHub:

```
deactivate
```

Luego, en la línea de comandos:

```
git add .
git commit -m "Mensaje descriptivo de tus cambios"
git push
```

6. Volver a abrir el proyecto:

Cuando desees reabrir el proyecto en otro momento o en otra máquina, sigue estos pasos:

Navega a la carpeta del proyecto en la línea de comandos.

Activa el entorno virtual:

```
venv\Scripts\activate
```

Descarga los cambios más recientes desde GitHub:

```
git pull
```

Instala los paquetes desde el archivo requirements.txt:

```
pip install -r requirements.txt
```

Recuerda que siempre es una buena práctica cargar tus cambios en GitHub antes de dejar de trabajar y asegurarte de tener los cambios más recientes cuando vuelvas a abrir el proyecto. Esto te ayuda a mantener un registro de tus cambios y a colaborar con otros desarrolladores de manera efectiva.
