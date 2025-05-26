# TuPrimeraPaginaGalzerano

## Cómo probar el proyecto

1. Crear entorno virtual y activarlo:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # en Windows
   ```

2. Instalar Django:
   ```bash
   pip install django
   ```

3. Aplicar migraciones:
   ```bash
   python manage.py migrate
   ```

4. Ejecutar el servidor:
   ```bash
   python manage.py runserver
   ```

5. Acceder a:
   - `/` para ver inicio
   - `/cursos/`, `/profesores/`, `/entregables/` para cargar datos
   - `/buscar/` para buscar curso por nombre

