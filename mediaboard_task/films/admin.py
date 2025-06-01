from django.contrib import admin
from .models import Film, Actor


class FilmInline(admin.TabularInline):
    model = Film.actors.through
    extra = 1


class ActorAdmin(admin.ModelAdmin):
    inlines = [FilmInline]
    list_display = ["name"]
    ordering = ["name"]


class FilmAdmin(admin.ModelAdmin):
    list_display = ["title", "rank"]
    ordering = ["rank"]


admin.site.register(Actor, ActorAdmin)
admin.site.register(Film, FilmAdmin)
