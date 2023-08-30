from distutils.log import Log
from re import template
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Message



class MessageListView(ListView):
    template_name = 'messenger/list.html'
    model = Message

class MessageDetailView(DetailView):
    template_name = 'messenger/detail.html'
    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    template_name = "messenger/add.html"
    model = Message
    fields = '__all__'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    success_url = reverse_lazy('message_list')



class MessageUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "messenger/edit.html"
    model = Message
    fields = '__all__'
    success_url = reverse_lazy('message_list')


class MessageDeleteView(LoginRequiredMixin,DeleteView):
    model = Message
    template_name = 'messenger/delete.html'
    success_url = reverse_lazy('message_list')



