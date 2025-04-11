# Herencia en Django

Este proyecto sirve como base para la clase de Herencia y Polimorfismo en Django. A través del código, se exploran conceptos como herencia de modelos, relaciones polimórficas entre clases y cómo aplicar buenas prácticas para estructurar modelos reutilizables y extensibles en una aplicación Django.

## Requisitos previos

- Python 3.8 o superior
- MySQL instalado y corriendo
- `pip` y `venv` disponibles

## Configuración del entorno de desarrollo

1. **Clona el repositorio:**

```bash
git clone https://github.com/camigomezdev/herencia_django.git
cd herencia_django
```

2. **Crea y activa un entorno virtual:**

```bash
python -m venv env
source env/bin/activate  # En Windows usa: env\Scripts\activate
```

3. **Instala las dependencias:**

```bash
pip install -r requirements.txt
```

4. **Configura la base de datos MySQL:**

Asegúrate de tener una base de datos creada y configura tus credenciales en el archivo `settings.py` o usando variables de entorno. Ejemplo:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nombre_base_de_datos',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

5. **Ejecuta migraciones:**

```bash
python manage.py migrate
```

6. **Crea un superusuario (opcional):**

```bash
python manage.py createsuperuser
```

7. **Corre el servidor de desarrollo:**

```bash
python manage.py runserver
```

## Otros comandos útiles

- Ver estado de migraciones:

```bash
python manage.py showmigrations
```

- Aplicar migraciones pendientes:

```bash
python manage.py migrate
```

- Crear nuevas migraciones:

```bash
python manage.py makemigrations
```

## Notas

- Asegúrate de que el conector de MySQL para Python esté instalado. Si no lo está, puedes instalarlo con:

```bash
pip install mysqlclient
```

En sistemas Linux, puede que necesites instalar previamente:

```bash
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
```
