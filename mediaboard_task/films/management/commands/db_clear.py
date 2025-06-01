from django.core.management.base import BaseCommand
from films.models import Film, Actor


class Command(BaseCommand):
    help = "Clears all data from Film and Actor tables"

    def handle(self, *args, **options):
        try:
            num_films_deleted, _ = Film.objects.all().delete()
            self.stdout.write(
                self.style.SUCCESS(f"Successfully deleted {num_films_deleted} films.")
            )
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error deleting films: {e}"))

        try:
            num_actors_deleted, _ = Actor.objects.all().delete()
            self.stdout.write(
                self.style.SUCCESS(f"Successfully deleted {num_actors_deleted} actors.")
            )
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error deleting actors: {e}"))

        self.stdout.write(
            self.style.SUCCESS("Finished clearing Film and Actor tables.")
        )
