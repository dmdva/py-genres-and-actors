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

    actors_data = [
        ("George", "Klooney"),
        ("Kianu", "Reaves"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Keegan"),
        ("Scarlett", "Johansson"),
    ]

    actors_to_create = [
        Actor(first_name=first, last_name=last) for first, last in actors_data
    ]

    Genre.objects.bulk_create(genres)
    Actor.objects.bulk_create(actors_to_create)

    Genre.objects.filter(
        name="Dramma",
    ).update(name="Drama")

    Actor.objects.filter(
        last_name="Klooney",
    ).update(last_name="Clooney")

    Actor.objects.filter(
        first_name="Kianu",
        last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(
        name="Action",
    ).delete()

    Actor.objects.filter(
        first_name="Scarlett",
    ).delete()

    return Actor.objects.filter(
        last_name="Smith"
    ).order_by("first_name")
