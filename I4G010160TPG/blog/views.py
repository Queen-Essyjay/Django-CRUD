from pyexpat import model
from venv import create
from django import views
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog.models import Post

# Create your views here.
class PostListView(ListView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = '_all__'
    success_url  = reverse_lazy('blog:all')

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post
    fields = '_all__'
    success_url  = reverse_lazy('blog:all')

class PostDeleteView(DeleteView):
    model = Post
    fields = '_all__'
    success_url  = reverse_lazy('blog:all')