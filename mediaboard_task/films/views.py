from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import generic

from .models import Film, Actor


def search(request: HttpRequest) -> HttpResponse:
    context = {
        "result": False,
    }
    query = request.GET.get("query", "")
    if query:
        films = Film.objects.filter(search_field__acicontains=query).order_by("rank")
        actors = Actor.objects.filter(search_field__acicontains=query).order_by("name")
        context = {
            "films": films,
            "actors": actors,
            "query": query,
            "result": True,
        }

    return render(request, "films/search.html", context)


class FilmDetailView(generic.DetailView):
    model = Film
    template_name = "films/film_detail.html"
    context_object_name = "film"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["actors"] = self.object.actors.all()
        return context


class ActorDetailView(generic.DetailView):
    model = Actor
    template_name = "films/actor_detail.html"
    context_object_name = "actor"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["films"] = self.object.films.all()
        return context
