from django.shortcuts import render
from django.http import HttpResponse
from .models import Articale

def home(request):
    posts = Articale.objects.order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

def test(request):
    return HttpResponse ('<h1>Test page</h1>')
