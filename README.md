# Proyecto "Vidas sobre ruedas" - Natalia Chehda

Este es un proyecto web llamado "Vidas sobre ruedas" que tiene como objetivo compartir historias inspiradoras de personas que viven con discapacidad y utilizan sillas de ruedas. El proyecto consta de dos aplicaciones: una aplicación de blog y otra aplicación relacionada con meetups y eventos.

## Tecnologías utilizadas

El proyecto se ha desarrollado utilizando las siguientes tecnologías:

- Python
- Django (framework de desarrollo web en Python)
- HTML
- CSS (con el uso de Bootstrap para la maquetación)
- JavaScript (principalmente para el uso de Bootstrap y algunas funcionalidades adicionales)

## Estructura del proyecto

El proyecto está estructurado en las siguientes partes principales:

- **AppCoder**: Esta es la aplicación principal del proyecto que contiene las vistas y plantillas para las páginas principales del sitio web, como la página de inicio, las historias personales, los meetups, las preguntas y respuestas, y el perfil del usuario.
- **Blog**: Esta es una aplicación secundaria que se encarga de gestionar los blogs y las historias de vida en sillas de ruedas. Contiene modelos para los blogs, formularios para la creación y edición de blogs, y vistas relacionadas.
- **Media**: Esta carpeta almacena los archivos multimedia del proyecto, como las imágenes de los blogs y los avatares de los usuarios.

## Funcionalidades principales

El proyecto cuenta con las siguientes funcionalidades principales:

- Registro y autenticación de usuarios: Los usuarios pueden registrarse en el sitio web y luego iniciar sesión para acceder a las funcionalidades exclusivas para usuarios autenticados.
- Publicación de blogs y historias de vida: Los usuarios autenticados pueden crear y publicar sus propios blogs y compartir sus historias de vida en sillas de ruedas.
- Visualización de blogs y historias de vida: Los visitantes del sitio web pueden leer los blogs y las historias de vida publicadas por los usuarios.
- Gestión de meetups y eventos: Los usuarios autenticados pueden crear, editar y eliminar meetups y eventos relacionados con la comunidad de personas en sillas de ruedas.
- Búsqueda de contenido: Los usuarios pueden buscar blogs, historias de vida, meetups y eventos utilizando un campo de búsqueda.

## Configuración del entorno de desarrollo

Para configurar el entorno de desarrollo y ejecutar el proyecto en tu máquina local, sigue los siguientes pasos:

1. Asegúrate de tener instalado Python en tu sistema.
2. Clona este repositorio en tu máquina local.
3. Crea un entorno virtual para el proyecto e instala las dependencias del proyecto utilizando el archivo `requirements.txt`.
4. Configura la base de datos según tu preferencia en el archivo `settings.py`.
5. Ejecuta las migraciones para crear las tablas de la base de datos.
6. Ejecuta el servidor de desarrollo de Django y accede al sitio web desde tu navegador.
