from django.shortcuts import render
from django.http import HttpResponse
from familiar.models import Familiar

# Create your views here.
def crear_familiar(request):
    Familiar.objects.create(name='Jose', edad=54, casado=True)
    return HttpResponse('familiar')

def lista_familiar(request):
    familiares = Familiar.objects.all()
    print(familiares)
    context = {
        'familiares': familiares,
    }
    return render(request, 'lista_familiar.html', context=context)

