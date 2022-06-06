from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def inicio(request):
    return render(request, 'AppBlog/inicio.html')

def cafe(request):
    return render(request, 'AppBlog/cafe.html')

def platos(request):
    return render(request, 'AppBlog/platos.html')

def postres(request):
    return render(request, 'AppBlog/postres.html')

def quesos(request):
    return render(request, 'AppBlog/quesos.html')

def vinos(request):
    return render(request, 'AppBlog/vinos.html')




