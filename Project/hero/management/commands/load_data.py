from json import loads
from django.core.management.base import BaseCommand
from pathlib import Path
from hero.models import Superhero

class Command(BaseCommand):
    def handle(self, *args, **options):
        load_data()

def load_data():
    Superhero.objects.all().delete()

    path = Path('hero_objects.json')
    if path.exists():
        objects = loads(path.read_text())
    
    for o in objects:
        Superhero.objects.get_or_create(**o)

    for hero in Superhero.objects.all().values():
        print(hero)