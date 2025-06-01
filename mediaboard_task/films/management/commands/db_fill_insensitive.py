from django.core.management.base import BaseCommand
from unidecode import unidecode

from films.models import Film, Actor


class Command(BaseCommand):
    help = "Create accent insensitive search fields for films and actors"

    def handle(self, *args, **options):
        for film in Film.objects.all():
            film.search_field = unidecode(film.title.lower())
            film.save()
        for actor in Actor.objects.all():
            actor.search_field = unidecode(actor.name.lower())
            actor.save()
        self.stdout.write(
            self.style.SUCCESS("Successfully updated search_field for all films.")
        )
