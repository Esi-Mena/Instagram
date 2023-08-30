from distutils.log import Log
from re import template
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Article



class ArticleListView(ListView):
    template_name = 'article/list.html'
    model = Article

class ArticleDetailView(DetailView):
    template_name = 'article/detail.html'
    model = Article


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "article/add.html"
    model = Article
    fields = '__all__'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    success_url = reverse_lazy('article_list')



class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "article/edit.html"
    model = Article
    fields = '__all__'
    success_url = reverse_lazy('article_list')


class ArticleDeleteView(LoginRequiredMixin,DeleteView):
    model = Article
    template_name = 'article/delete.html'
    success_url = reverse_lazy('article_list')



