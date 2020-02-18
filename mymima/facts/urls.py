from django.urls import path

from . import views

app_name = "facts"

urlpatterns = [
    path('', views.home, name="home"),
    path('artist/<str:let>', views.artists, name="artists"),
    path('song/<str:let>', views.songs, name="songs"),
    path('song_artist/<str:name>', views.songs_by_artist, name="song_by_artist"),
    path('facts/<str:song>/<str:artist>', views.facts, name="facts"),
    path('search', views.search, name="search"),
    path('add/', views.add_fact, name="add")
    ]