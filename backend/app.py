from flask import Flask, render_template, request, redirect, url_for, flash, abort

# importa las funciones de la base de datos
from models import init_db, get_all_movies, get_movie_by_id, save_contact, save_movie


# inicializa la aplicacion
app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

# clave secreta para los mensajes flash
app.config['SECRET_KEY'] = 'tu-clave-secreta-cambiame'


# ruta de la pagina de inicio
@app.route("/")
def index():
    return render_template("index.html")


# ruta de la pagina sobre mi
@app.route("/about")
def about():
    return render_template("about.html")


# muestra todas las peliculas de la base de datos
@app.route("/movies", endpoint="movies")
def movies_list():

    movies = get_all_movies()

    return render_template("movies.html", movies=movies)


# formulario para añadir peliculas
@app.route("/add_movie", methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        director = request.form.get('director', '').strip()
        year = request.form.get('year', '').strip()
        genre = request.form.get('genre', '').strip()
        description = request.form.get('description', '').strip()
        rating = request.form.get('rating', '').strip()
        poster_url = request.form.get('poster_url', '').strip()

        if not title:
            flash('El titulo es obligatorio.', 'error')
            return redirect(url_for('add_movie'))

        try:
            year = int(year) if year else None
            rating = float(rating) if rating else 0.0
        except ValueError:
            flash('El año o la puntuacion no son validos.', 'error')
            return redirect(url_for('add_movie'))

        if rating < 0 or rating > 10:
            flash('La puntuacion debe estar entre 0 y 10.', 'error')
            return redirect(url_for('add_movie'))

        save_movie(title, director, year, genre, description, rating, poster_url)
        flash('Pelicula añadida correctamente.', 'success')
        return redirect(url_for('movies'))

    return render_template('add_movie.html')


# muestra los detalles de una pelicula
@app.route("/movie/<int:movie_id>")
def movie_detail(movie_id):

    # busca la pelicula por su id
    movie = get_movie_by_id(movie_id)

    # si no existe muestra el error 404
    if not movie:
        abort(404)

    return render_template("movie_detail.html", movie=movie)


# formulario de contacto
@app.route("/contact", methods=['GET', 'POST'])
def contact():

    # comprueba si se ha enviado el formulario
    if request.method == 'POST':

        # recoge los datos del formulario
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # comprueba que los campos obligatorios no esten vacios
        if not name or not email or not message:
            flash('Por favor rellena todos los campos requeridos.', 'error')
            return redirect(url_for('contact'))

        # guarda el mensaje en la base de datos
        save_contact(name, email, subject, message)

        # muestra un mensaje de confirmacion
        flash('Gracias por tu mensaje — te responderemos pronto.', 'success')

        return redirect(url_for('contact'))

    return render_template("contact.html")


# muestra la pagina de error 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# muestra la pagina de error 500
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


# inicializa la base de datos y añade las peliculas si esta vacia
def initialize_app():

    # crea las tablas de la base de datos
    init_db()

    # obtiene las peliculas guardadas
    movies = get_all_movies()

# inicia la aplicacion
if __name__ == "__main__":

    initialize_app()

    app.run(debug=True)