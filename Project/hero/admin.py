from django.contrib import admin
from .models import Superhero, Article, Photo, Message
# Register your models here.
admin.site.register(Superhero)
admin.site.register(Article)
admin.site.register(Photo)
admin.site.register(Message)
