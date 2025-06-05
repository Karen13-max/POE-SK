Proyecto Editorial Andina S.A.S.


Aplicación de escritorio desarrollada con Python que permite la gestión de autores y libros de forma sencilla. Incluye un backend en Django REST Framework para almacenamiento y un frontend en Tkinter con funcionalidades completas, además de copias de seguridad automáticas.

Descripción del Proyecto

La aplicación permite:

- Registrar, consultar, actualizar y eliminar autores y libros.

- Visualizar registros en tablas.

- Realizar respaldos automáticos de los datos en archivos de texto (respaldo_autores.txt y respaldo_libros.txt) cada minuto.


Estructura del Proyecto

proyecto_editorial
     ├── backend_editorial│   
        ├── autor
        ├── editorial
        |── libro
     └── manage.py
     ├── frontend_editorial  
        ├── controladores (Comunicaciones y validaciones)  
            └── respaldo_autores.txt y respaldo_libros.txt (Respaldos automáticos)
        ├── modelos (Clases Autor y Libro) 
        ├── vistas (Interfaz gráfica Tkinter) 
     ├── __main__.py (Entrada principal del frontend)│   
     └── __init__.py
     ├── README.md (Este archivo)└── respaldo_autores.txt y respaldo_libros.txt (Respaldos automáticos)


Instalación y Configuración

1️⃣ Requisitos:

- Python 3.x instalado.

- Bibliotecas necesarias: django, djangorestframework, requests, tkinter (incluido en Python), time, datetime, megabox.

- Conexión a localhost para las pruebas.

2️⃣ Instalación del Backend (Django):

cd backend_editorial

# En Windows usa 

pip install django djangorestframework

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

3️⃣ Instalación del Frontend (Tkinter):

cd frontend_editorial

pip install requests

python __main__.py


Instrucciones de Uso

1️⃣ Iniciar el backend:

- Ejecuta el servidor de Django para exponer la API REST.

2️⃣ Iniciar la aplicación:

- Abre la ventana de gestión con Tkinter.

- La interfaz mostrará dos pestañas: Autores y Libros.

- Completa los formularios para registrar nuevos autores/libros.

- Usa los botones para consultar, actualizar, eliminar y consultar todos.

- Las tablas mostrarán los registros de cada tipo.

3️⃣ Copias de seguridad automáticas:

- Se crean cada minuto mientras la aplicación esté abierta.

- Los archivos se guardan como respaldo_autores.txt y respaldo_libros.txt en la carpeta raíz.


Notas de Seguridad

- La aplicación es de uso interno y se ejecuta localmente.

- Los respaldos sobrescriben los archivos anteriores automáticamente.


Consideraciones

- Puedes modificar el código para personalizar los campos o agregar validaciones adicionales.

- La interfaz puede extenderse para incluir búsquedas o filtros avanzados.



Karen Dayana Campuzano Burgos 

Santiago Velasco Ramos 




