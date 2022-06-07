from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppBlog.models import Vino
from AppBlog.forms import Formulario
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
    
    if request.method == 'POST':
        formulario = Formulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            vino = Vino(varietal = informacion['varietal'], origen = informacion['origen'], fecha = informacion['fecha'], temperatura = informacion['temperatura'])
            vino.save()
        return render(request, "AppBlog/inicio.html")
    else:
        formulario = Formulario()
        
    return render(request, "AppBlog/vinos.html", {"formulario":formulario})

def busquedaVinos(request):

    return render(request, 'AppBlog/busquedaVinos.html')

def buscar(request):

    if request.GET['varietal']:

        varietal = request.GET['varietal']
        info = Vino.objects.filter(varietal__icontains=varietal)

        return render(request, "AppBlog/resultadoBusqueda.html", {'varietal':varietal, 'info':info})
    else:
        respuesta = "No hay datos"

    return HttpResponse(respuesta)







