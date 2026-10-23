import sqlite3

# crea la base de datos y sus tablas
def init_db():
    conn = sqlite3.connect('proyecto.db')
    cursor = conn.cursor()

    # crea la tabla de peliculas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            director TEXT,
            year INTEGER,
            genre TEXT,
            description TEXT,
            rating REAL DEFAULT 0.0,
            poster_url TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # crea la tabla de contactos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            subject TEXT,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

    print("Base de datos inicializada")

# obtiene todas las peliculas de la base de datos
def get_all_movies():
    conn = sqlite3.connect('proyecto.db')

    # permite acceder a los datos por el nombre de la columna
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM movies ORDER BY created_at DESC')

    movies = cursor.fetchall()

    conn.close()

    return movies


# busca una pelicula por su id
def get_movie_by_id(movie_id):
    conn = sqlite3.connect('proyecto.db')
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    # busca la pelicula que tenga ese id
    cursor.execute('SELECT * FROM movies WHERE id = ?', (movie_id,))

    movie = cursor.fetchone()

    conn.close()

    return movie


# guarda los mensajes del formulario de contacto
def save_contact(name, email, subject, message):
    conn = sqlite3.connect('proyecto.db')
    cursor = conn.cursor()

    # inserta el mensaje en la tabla de contactos
    cursor.execute('''
        INSERT INTO contacts (name, email, subject, message)
        VALUES (?, ?, ?, ?)
    ''', (name, email, subject, message))

    conn.commit()
    conn.close()

    print("Contacto guardado:", name)

# guarda una pelicula nueva en la base de datos
def save_movie(title, director, year, genre, description, rating, poster_url):
    conn = sqlite3.connect('proyecto.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO movies (title, director, year, genre, description, rating, poster_url)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (title, director, year, genre, description, rating, poster_url))

    conn.commit()
    conn.close()
    print('Pelicula guardada:', title)
