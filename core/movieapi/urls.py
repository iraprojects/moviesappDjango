from django.urls import path
from .views import (
    MoviesListApiView,
    MoviesDetailApiView,
    ReviewListApiView,
    ReviewDetailApiView,
    MovieStatsApiView
)

urlpatterns = [
    path("movies/", MoviesListApiView.as_view()),
    path("movies/<int:pk>/", MoviesDetailApiView.as_view()),
    path("reviews/", ReviewListApiView.as_view()),
    path("reviews/<int:pk>/", ReviewDetailApiView.as_view()),
    path('movie-stats/', MovieStatsApiView.as_view(), name='movie-stats'),
]
