<div align="center">

# 🎬 CineFlask

### Tu catálogo de películas, desarrollado con Flask

**Aplicación web para consultar y gestionar películas con Python, Flask y SQLite.**

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Jinja2](https://img.shields.io/badge/Jinja2-Templates-B41717?style=for-the-badge)

</div>

---

## 📌 Sobre el proyecto

**CineFlask** es una aplicación web desarrollada como parte de las actividades del módulo de **Optativa**, correspondiente al ciclo formativo de **Desarrollo de Aplicaciones Web (DAW)**.

El proyecto permite consultar un catálogo de películas y visualizar información sobre ellas. Además, incorpora un formulario para registrar nuevas películas y almacenar sus datos en una base de datos SQLite.

La aplicación está desarrollada con Flask y utiliza plantillas Jinja2 para generar las páginas HTML, junto con Bootstrap para mejorar la presentación visual.

## ✨ Funcionalidades

- 🎞️ **Catálogo de películas:** consulta las películas disponibles.
- 🔎 **Detalles de películas:** visualiza información específica de cada película.
- ➕ **Añadir películas:** registra nuevas películas mediante un formulario.
- 💾 **Base de datos SQLite:** almacena la información de las películas.
- 📩 **Formulario de contacto:** permite enviar mensajes desde la aplicación.
- 📄 **Plantillas Jinja2:** reutiliza una plantilla base para mantener una estructura común.
- 🎨 **Diseño con Bootstrap:** proporciona una interfaz clara y adaptable.

## 🛠️ Tecnologías utilizadas

| Tecnología | Utilidad |
|---|---|
| Python | Lenguaje de programación del servidor. |
| Flask | Desarrollo de la aplicación web y gestión de rutas. |
| SQLite | Almacenamiento de los datos. |
| Jinja2 | Generación de páginas HTML dinámicas. |
| HTML5 | Estructura de las páginas web. |
| CSS3 | Estilos y presentación visual. |
| Bootstrap | Componentes y diseño adaptable. |
| Git y GitHub | Control de versiones y alojamiento del código. |

## 📂 Estructura del proyecto

```text
CineFlask/
│
├── backend/
│   ├── app.py
│   ├── models.py
│   └── proyecto.db
│
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   │
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── movies.html
│       ├── movie_detail.html
│       ├── add_movie.html
│       ├── contact.html
│       └── about.html
│
├── requirements.txt
└── README.md
```

## ⚙️ Instalación y ejecución

Sigue estos pasos para ejecutar el proyecto en tu ordenador.

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU-USUARIO/Practica-Flask.git
```

Entra en la carpeta descargada:

```bash
cd Practica-Flask
```

### 2. Crear un entorno virtual

```bash
python -m venv venv
```

Actívalo según tu sistema operativo.

**Windows (CMD):**

```bash
venv\Scripts\activate
```

**Windows (Git Bash):**

```bash
source venv/Scripts/activate
```

**Linux:**

```bash
source venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Iniciar la aplicación

Entra en la carpeta del servidor:

```bash
cd backend
```

Ejecuta la aplicación:

```bash
python app.py
```

### 5. Abrir en el navegador

Accede a la siguiente dirección:

```text
http://127.0.0.1:5000
```

¡Ya puedes explorar CineFlask! 🍿

## ➕ Añadir una película

La aplicación incorpora un formulario para registrar nuevas películas.

1. Abre CineFlask en el navegador.
2. Accede a la opción **Añadir película** del menú.
3. Introduce los datos de la película.
4. Pulsa **Guardar película**.
5. Comprueba que aparece en el catálogo.

Los datos se almacenan en la base de datos SQLite para poder consultarlos desde la aplicación.

## 🎓 Información académica

| Dato | Información |
|---|---|
| Ciclo formativo | Desarrollo de Aplicaciones Web (DAW) |
| Curso | Segundo curso |
| Módulo | Optativa |
| Proyecto | CineFlask |
| Alumno | Vicente Ayuso Pino |

## 🚀 Objetivos de aprendizaje

Con este proyecto se trabajan diferentes aspectos del desarrollo web del lado del servidor:

- Creación de aplicaciones web con Flask.
- Definición de rutas y gestión de peticiones HTTP.
- Uso de formularios HTML con los métodos GET y POST.
- Renderizado de plantillas mediante Jinja2.
- Conexión con bases de datos SQLite.
- Ejecución de consultas SQL para almacenar y recuperar información.
- Organización de archivos en un proyecto web.
- Control de versiones mediante Git y GitHub.

## 📌 Estado del proyecto

🚧 **En desarrollo.**

El proyecto se amplía progresivamente mediante las actividades prácticas del módulo de Optativa.

---

<div align="center">

**🎬 CineFlask · 2.º DAW · Optativa**

*Desarrollado por Vicente Ayuso Pino*

</div>
