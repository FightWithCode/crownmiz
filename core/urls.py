from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
    # Songs
    path('songs/create/', views.CreatSongView.as_view(), name='song-create'),
    path('songs/', views.AllSongView.as_view(), name='all-songs'),
    path('songs/<int:id>', views.SongView.as_view(), name='single-song'),
    # Movies
    path('movies/create/', views.CreatMovieView.as_view(), name='song-create'),
    path('movies/', views.AllMovieView.as_view(), name='all-songs'),
    path('movies/<int:id>', views.MovieView.as_view(), name='single-song'),
]
