from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('delete/<int:image_id>/', views.delete_image, name='delete_image'),
]
