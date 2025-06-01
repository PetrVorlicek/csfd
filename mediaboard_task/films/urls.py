from django.urls import path

from .views import search, FilmDetailView, ActorDetailView

app_name = "films"
urlpatterns = [
    path("", search, name="search"),
    path("film/<int:pk>/", FilmDetailView.as_view(), name="film_detail"),
    path("actor/<int:pk>/", ActorDetailView.as_view(), name="actor_detail"),
]
