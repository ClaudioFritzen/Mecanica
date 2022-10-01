from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.
def clientes(request):
    return render(request, 'clientes.html')