from django.shortcuts import render 
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from .models import Article
from django.urls import reverse_lazy

# Create your views here.

class ArticlesListView(ListView):
  model = Article
  template_name = "articles_list.html"

class ArticleDetailView(DetailView):
  model = Article
  template_name = "article_detail.html"

class ArticleUpdateView(UpdateView):
  model = Article
  template_name = "article_update.html"
  fields = ["title","body"]

class ArticleDeleteView(DeleteView):
  model = Article
  template_name = "article_delete.html"
  success_url = reverse_lazy("article_list")

class ArticleCreateView(CreateView):
  model = Article
  template_name = "article_create.html"
  fields = ["title","author","body"]