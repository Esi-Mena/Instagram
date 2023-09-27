from django.contrib import admin
from .models import Like, Comment, Photo, UserProfile
# Register your models here.
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Photo)
admin.site.register(UserProfile)
