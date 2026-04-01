import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:

    genres_names = [
        "Western",
        "Action",
        "Dramma",
    ]

    genres = [
        Genre(name=name) for name in genres_names
    ]

    actors = [
        Actor(
            first_name="George",
            last_name="Klooney"
        ),
        Actor(
            first_name="Kianu",
            last_name="Reaves"
        ),
        Actor(
            first_name="Will",
            last_name="Smith"
        ),
        Actor(
            first_name="Jaden",
            last_name="Smith"
        ),
    ]

    actresses = [
        Actor(
            first_name="Scarlett",
            last_name="Keegan"
        ),
        Actor(
            first_name="Scarlett",
            last_name="Johansson"
        ),
    ]

    Genre.objects.bulk_create(genres)
    Actor.objects.bulk_create(actors + actresses)

    Genre.objects.filter(
        name="Dramma",
    ).update(name="Drama")

    Actor.objects.filter(
        last_name="Klooney",
    ).update(last_name="Clooney")

    Actor.objects.filter(
        first_name="Kianu",
    ).update(first_name="Keanu")

    Actor.objects.filter(
        last_name="Reaves",
    ).update(last_name="Reeves")

    Genre.objects.filter(
        name="Action",
    ).delete()

    Actor.objects.filter(
        first_name="Scarlett",
    ).delete()

    return Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
