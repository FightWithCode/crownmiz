from django.urls import path
from artists import views

app_name = "artists"

urlpatterns = [
    path('create/', views.CreatArtistView.as_view(), name='artist-create'),
    path('', views.AllArtistView.as_view(), name='all-artists'),
    path('<int:id>', views.ArtistView.as_view(), name='single-artist'),
]
