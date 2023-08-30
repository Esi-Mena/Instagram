from distutils.log import Log
from re import template
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Superhero, Photo


class HeroListView(ListView):
    template_name = 'hero/list.html'
    model = Superhero


class HeroDetailView(DetailView):
    template_name = 'hero/detail.html'
    model = Superhero


class HeroCreateView(LoginRequiredMixin, CreateView):
    template_name = "hero/add.html"
    model = Superhero
    fields = '__all__'



class HeroUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "hero/edit.html"
    model = Superhero
    fields = '__all__'


class HeroDeleteView(LoginRequiredMixin,DeleteView):
    model = Superhero
    template_name = 'hero/delete.html'
    success_url = reverse_lazy('hero_list')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "registration/settings.html"
    model = User
    fields = ['first_name', 'last_name', 'username', 'email']
    success_url = reverse_lazy('hero_list')

class PhotoCreateView(LoginRequiredMixin, CreateView):
    template_name = "photos/add.html"
    model = Photo
    fields = '__all__'
    success_url = reverse_lazy('photo_list')

class PhotoListView(ListView):
    template_name= "photos/list.html"
    model = Photo
    context_object_name = 'photos'
class PhotoDetailView(DetailView):
    template_name = 'photos/detail.html'
    model = Photo
class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "photos/edit.html"
    model = Photo
    fields = '__all__'
class PhotoDeleteView(LoginRequiredMixin,DeleteView):
    model = Photo
    template_name = 'photos/delete.html'
    success_url = reverse_lazy('photo_list')
class PhotoCarouselView(TemplateView):
    template_name = 'photos/carousel.html'

    def get_context_data(self, **kwargs):
        photos = Photo.objects.all()
        carousel = carousel_data(photos)
        return dict(title='Carousel View', carousel=carousel)


def carousel_data(photos):

    def photo_data(id, image):
        x = dict(image_url=f"/media/{image}", id=str(id), label=f"{image} {id}")
        if id == 0:
            x.update(active="active", aria='aria-current="true"')
        return x

    return [photo_data(id, photo.image) for id, photo in enumerate(photos)]


