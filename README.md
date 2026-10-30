# Entrega final: Consolidación del Blog Web en GitHub

Aplicacion web de blog desarrollada como entrega final. Permite que las personas se registren, inicien sesion y creen publicaciones con imagenes.

## Tecnologias

- Python 3
- Django
- SQLite
- Pillow
- HTML y CSS

## Funcionalidades

- Listado y detalle de publicaciones.
- Creacion, edicion y eliminacion de posts desde la interfaz web.
- Carga opcional de imagenes para los posts.
- Busqueda por titulo o contenido.
- Registro, inicio y cierre de sesion.
- Proteccion de las rutas para crear, editar y eliminar publicaciones.
- Solo el autor de un post puede modificarlo o eliminarlo.

## Instalacion y ejecucion

1. Clonar el repositorio y entrar en su carpeta:

   ```bash
   git clone URL_DEL_REPOSITORIO
   cd entrega-final-python
   ```

2. Crear y activar un entorno virtual:

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```

3. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Aplicar las migraciones:

   ```bash
   python manage.py migrate
   ```

5. Iniciar el servidor:

   ```bash
   python manage.py runserver
   ```

6. Abrir `http://127.0.0.1:8000/` en el navegador.

La base de datos e imagenes de usuarios no se incluyen en el repositorio. Luego de ejecutar las migraciones, podes crear una cuenta desde `/registro/` y cargar tus propios posts.

## Panel de administracion

Para usar el panel de Django, crear un superusuario:

```bash
python manage.py createsuperuser
```

Despues ingresar en `http://127.0.0.1:8000/admin/`.

## Autor

Tadeo Collado — entrega final de Python y Django.