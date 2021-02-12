# from django.shortcuts import render
from django.views.generic import ListView
from .models import Article

# Create your views here.
class ArticleList(ListView):
	def get_queryset(self):
		return Article.objects.filter(status=True)