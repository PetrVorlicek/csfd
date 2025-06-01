from django.core.management.base import BaseCommand
from films.models import Film, Actor

from src.agent import fetch_page, get_ledger_suffix
from src.parser import parse_elements, parse_movie_details


class Command(BaseCommand):
    help = "Scrape CSFD for the best movies and save them to the database."
    BASE_URL = "https://www.csfd.cz/"
    rank_current = 0

    def fetch_movie_urls_from_ledger(self, ledger_index: int) -> list[str]:
        """
        Fetch the list of movie title URLs from the given URL.
        """
        url = self.BASE_URL + get_ledger_suffix(ledger_index)
        page_text = fetch_page(url)
        return parse_elements(page_text, ".article-poster-60 figure a")

    def fetch_and_save_movie_info(self, title_url: str):
        """
        Fetch movie details from the given title URL and save to the database.
        """

        film_url = self.BASE_URL + title_url
        page_text = fetch_page(film_url)
        title, actors = parse_movie_details(page_text)

        self.rank_current += 1
        film, created = Film.objects.get_or_create(rank=self.rank_current, title=title)
        if not created:
            raise ValueError(
                f"Film with rank {self.rank_current} and title '{title}' already exists."
            )

        if actors:  # There are films like Krteček that have no actors listed.
            for actor_name in actors:
                actor, _ = Actor.objects.get_or_create(name=actor_name)
                film.actors.add(actor)
        else:
            self.stdout.write(self.style.WARNING(f"No actors found for film: {title}"))
        film.save()

    def scrape_movies_from_ledger(self, ledger_index: int):
        """
        Scrape a single page of the best movies.
        """

        movie_title_urls = self.fetch_movie_urls_from_ledger(ledger_index)
        self.stdout.write(
            f"Found {len(movie_title_urls)} movie titles on page {ledger_index + 1}."
        )

        # Check if we saved all films
        rank_old = self.rank_current
        errors = 0

        for title_url in movie_title_urls:
            self.stdout.write(f"Rank: {self.rank_current}\t title_url: {title_url}")

            try:
                self.fetch_and_save_movie_info(
                    title_url=title_url,
                )
            except ValueError:
                self.stdout.write(self.style.ERROR("Film already exists."))
                errors += 1

        # Check that we saved all films
        films_saved = self.rank_current - rank_old - errors
        if len(movie_title_urls) != films_saved:
            self.stdout.write(
                self.style.WARNING(
                    f"Expected {len(movie_title_urls)} films, but saved {films_saved}."
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully saved {films_saved} films from page {ledger_index}."
                )
            )

    def handle(self, *args, **options):

        for i in range(10):
            # This would be great place for threading,
            # as scraping and saving to DB is IO bound operation.
            # However it raises issues with simultaneous writes to DB,
            # as well as off-by-one errors in ranking.
            self.scrape_movies_from_ledger(i)

        self.stdout.write(self.style.SUCCESS("Scraping completed successfully!"))
