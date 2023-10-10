from django.contrib import admin
from django.urls import path, include
from pixlpix import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_view, name='landing'),
    path('home', views.home, name='home'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('upload/', views.upload_photo, name='upload_photo'),
    path('photo/<int:photo_id>/', views.photo_detail, name='photo_detail'),
    path('like/<int:photo_id>/', views.like_photo, name='like_photo'),
    path('unlike/<int:photo_id>/', views.unlike_photo, name='unlike_photo'),
    path('follow/<str:username>/', views.follow_user, name='follow_user'),
    path('unfollow/<str:username>/', views.unfollow_user, name='unfollow_user'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
