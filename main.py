import init_django_orm  # noqa: F401

from django.db.models import QuerySet


from db.models import Actor, Genre

def main() -> QuerySet:
    western = Genre.objects.create(name="Western")
    action = Genre.objects.create(name="Action")
    dramma = Genre.objects.create(name="Dramma")

    george = Actor.objects.create(first_name="George", last_name="Klooney")
    kianu = Actor.objects.create(first_name="Kianu", last_name="Reaves")
    scarlett = Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    will = Actor.objects.create(first_name="Will", last_name="Smith")
    jaden = Actor.objects.create(first_name="Jaden", last_name="Smith")
    scarlett_johansson = Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    dramma.name = "Drama"
    dramma.save()

    george.last_name = "Clooney"
    george.save()

    kianu.last_name = "Reeves"
    kianu.first_name = "Keanu"
    kianu.save()

    action.delete()

    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(last_name="Smith").order_by("first_name")






