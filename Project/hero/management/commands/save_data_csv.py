from csv import writer
from django.core.management.base import BaseCommand

from hero.models import Superhero

class Command(BaseCommand):
    def handle(self, *args, **options):
       save_data()

def save_data():
    for hero in Superhero.objects.all().values():
        print(hero)
    data = [[b.name, b.identity, b.description, b.image, b.strengths, b.weaknesses] for b in Superhero.objects.all()]

    with open('hero_objects.csv', "w", newline = '') as f:
        writer(f).writerows(data)