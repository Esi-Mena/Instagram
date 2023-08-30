
from django.urls import path, include
from django.views.generic import RedirectView
from .views import HeroCreateView, HeroDeleteView, HeroDetailView, HeroListView, HeroUpdateView, PhotoCreateView, SignUpView, UserUpdateView, PhotoListView, PhotoDeleteView, PhotoDetailView, PhotoUpdateView, PhotoCarouselView
from .views_articles import ArticleCreateView, ArticleListView, ArticleDeleteView, ArticleDetailView, ArticleUpdateView
from .views_message import MessageListView, MessageCreateView, MessageDeleteView, MessageDetailView, MessageUpdateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #Hero Views
    path('',                HeroListView.as_view(),    name='hero_list'),
    path('hero',                HeroListView.as_view(),    name='hero_list'),
    path('hero/<int:pk>',        HeroDetailView.as_view(),  name='hero_detail'),
    path('hero/add',             HeroCreateView.as_view(),  name='hero_add'),
    path('hero/<int:pk>/',       HeroUpdateView.as_view(),  name='hero_edit'),
    path('hero/<int:pk>/delete', HeroDeleteView.as_view(),  name='hero_delete'),
    #Account Views
    path('accounts/signup/', SignUpView.as_view(), name = 'signup'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    #Article Views
    path('article/',                  ArticleListView.as_view(),    name='article_list'),
    path('article/<int:pk>',          ArticleDetailView.as_view(),  name='article_detail'),
    path('article/add',               ArticleCreateView.as_view(),  name='article_add'),
    path('article/<int:pk>/',         ArticleUpdateView.as_view(),  name='article_edit'),
    path('article/<int:pk>/delete',   ArticleDeleteView.as_view(),  name='article_delete'),
    #Photo Views
    path('photo/add', PhotoCreateView.as_view(), name = 'photo_add'),
    path('photo', PhotoListView.as_view(), name = 'photo_list'),
    path('photo/<int:pk>', PhotoDetailView.as_view(), name = 'photo_detail'),
    path('photo/<int:pk>/', PhotoUpdateView.as_view(), name = 'photo_edit'),
    path('photo/<int:pk>/delete', PhotoDeleteView.as_view(), name = 'photo_delete'),
    path('photo/carousel',              PhotoCarouselView.as_view()),
    #Message Views
    path('message/',                  MessageListView.as_view(),    name='message_list'),
    path('message/<int:pk>',          MessageDetailView.as_view(),  name='message_detail'),
    path('message/add',              MessageCreateView.as_view(),  name='message_add'),
    path('message/<int:pk>/',         MessageUpdateView.as_view(),  name='message_edit'),
    path('message/<int:pk>/delete',   MessageDeleteView.as_view(),  name='message_delete'),
    


    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
