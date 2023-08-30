from csv import reader
from django.core.management.base import BaseCommand
from pathlib import Path
from hero.models import Superhero

class Command(BaseCommand):
    def handle(self, *args, **options):
        load_data()

def load_data():
    Superhero.objects.all().delete()
    for hero in Superhero.objects.all().values():
        print(hero)
    path = Path('hero_objects.csv')
    with open(path) as f:
        return[row for row in reader(f)]

    