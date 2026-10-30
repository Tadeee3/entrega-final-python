# Mi Blog Django

Aplicación web de blog desarrollada como proyecto final del curso de Python. Permite que las personas se registren, inicien sesión y creen publicaciones con imágenes.

## Tecnologías

- Python 3
- Django
- SQLite
- Pillow
- HTML y CSS

## Funcionalidades

- Listado y detalle de publicaciones.
- Creación, edición y eliminación de posts desde la interfaz web.
- Carga opcional de imágenes para los posts.
- Búsqueda por título o contenido.
- Registro, inicio y cierre de sesión.
- Protección de las rutas para crear, editar y eliminar publicaciones.
- Solo el autor de un post puede modificarlo o eliminarlo.

## Instalación y ejecución

1. Cloná el repositorio y entrá en su carpeta:

   ```bash
   git clone URL_DEL_REPOSITORIO
   cd blog_django
   ```

2. Creá y activá un entorno virtual:

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```

3. Instalá las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Aplicá las migraciones:

   ```bash
   python manage.py migrate
   ```

5. Iniciá el servidor:

   ```bash
   python manage.py runserver
   ```

6. Abrí `http://127.0.0.1:8000/` en el navegador.

La base de datos y las imágenes de usuarios no se incluyen en el repositorio. Luego de ejecutar las migraciones, podés crear una cuenta desde `/registro/` y cargar tus propios posts.

## Panel de administración

Para usar el panel de Django, creá un superusuario:

```bash
python manage.py createsuperuser
```

Después ingresá en `http://127.0.0.1:8000/admin/`.

## Autor

Tu Nombre — Proyecto final de Python y Django.
