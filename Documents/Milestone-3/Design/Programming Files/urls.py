from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_photo, name='upload_photo'),
    path('photo/<int:photo_id>/', views.photo_detail, name='photo_detail'),
    path('user/<str:username>/', views.user_profile, name='user_profile'),
    path('like/<int:photo_id>/', views.like_photo, name='like_photo'),
    path('follow/<str:username>/', views.follow_user, name='follow_user'),
]
