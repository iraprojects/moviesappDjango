#API de Películas y Reseñas

Rutas:
/movieapi/movies/
movieapi/reviews/
/movieapi/movie-stats/

Modelos:
Registrar Peliculas:
 {
        "title": "Wonka",
        "director": "Paul King",
        "release_date": "2023-12-23",
        "duration_minutes": 156,
        "synopsis": "Roald Dahl’s most iconic children's book and one of the best-selling children's books of all time",
        "genre": "Musical"
  }

  Resgistrar Reviews:
   {
        "user": "mrmafiaman",
        "review": "Una obra maestra del cine, la actuación es impresionante y la historia cautivadora.",
        "score": 5,
        "movie": 1
  },

Estadisticas:
{
        "movie_id": 1,
        "title": "El Padrino",
        "average_score": 3.5
},
