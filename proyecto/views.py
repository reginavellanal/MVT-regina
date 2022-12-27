from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
    return HttpResponse('hola')

def vista_con_template(request):
    return render(request, 'template.html', context={})

def saludo_desde_template(request):
    context = {
        'nombre': 'Regina',
        'edad': 23,
        'usa_lentes': True,
        'lista_frutas': ['manzana', 'pera', 'banana', 'naranja']
    }
    return render(request, 'saludo.html', context=context)