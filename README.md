TuPrimeraPaginaGalzerano
Proyecto final del curso de Python y Django - CoderHouse
Aplicación web estilo blog con herencia de plantillas, formularios, administración y diseño responsive.


📌 Cómo probar el proyecto
Clonar el repositorio:
git clone https://github.com/ElianaGalzerano/TuPrimeraPaginaGalzerano.git
cd TuPrimeraPaginaGalzerano

Crear entorno virtual y activarlo:
python -m venv venv
.\venv\Scripts\activate # En Windows

Instalar Django:
pip install django

Aplicar migraciones:
python manage.py makemigrations
python manage.py migrate

Crear superusuario (opcional para ver admin):
python manage.py createsuperuser

Ejecutar el servidor:
python manage.py runserver

Acceder a la app:

/ → Página de inicio

/cursos/ → Agregar curso

/profesores/ → Agregar profesor

/entregables/ → Agregar entregable

/buscar/ → Buscar curso por nombre

/admin/ → Panel de administración de Django

✅ Funcionalidades incluidas
✔️ Herencia de plantillas con base.html
✔️ Modelo con 3 clases (Curso, Profesor, Entregable)
✔️ Formularios para insertar datos desde el navegador
✔️ Formulario de búsqueda de cursos por nombre
✔️ Panel de administración (/admin) con modelos registrados
✔️ Estilos aplicados con Bootstrap 5
✔️ Banner visual con fondo decorativo
✔️ Footer con derechos de autor personalizado

🧠 Desarrollado como parte del curso de CoderHouse - Python
📅 Entrega: Mayo 2025
👩‍💻 Autora: Eliana Galzerano



