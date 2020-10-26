from articles.models import Article
from django.shortcuts import render
from django.http import HttpResponse
from django import template
from articles import models


def home(request):
    return HttpResponse(u'Hello Suchenki!')

def archive(request):
   return render(request, 'archive.html', {"posts": Article.objects.all()})
