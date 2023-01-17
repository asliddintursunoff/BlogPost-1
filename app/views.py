
from django.shortcuts import render

# Create your views here.
from app.models import Post
from django.views.generic import ListView
class PostViews(ListView):
    model = Post
    context_object_name = 'student'
    template_name = 'blog/index.html'

