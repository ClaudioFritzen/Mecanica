from pydoc import cli
import re
from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Cliente, Carro

from django.core import serializers
import json

# Create your views here.
def clientes(request):
    if request.method == "GET":
        clientes_list = Cliente.objects.all()
        return render(request, 'clientes.html', {'clientes': clientes_list })
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')

        carros = request.POST.getlist('carro')
        placas = request.POST.getlist('placa')
        anos = request.POST.getlist('ano')

        # fazendo a validação do cpf
        # buscando no banco se existe o cpf em todos os clientes no db
        cliente = Cliente.objects.filter(cpf=cpf)

        # se tiver faz
        if cliente.exists():
           return render(request, 'clientes.html', {'nome': nome, 'sobrenome': sobrenome, 'email': email, 'carros': zip(carros, placas, anos)})
           

        # validação do email
        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            return render(request, {'nome': nome, 'sobrenome': sobrenome, 'cpf': cpf, 'carros': zip(carros, placas, ano)})
           



        cliente = Cliente(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            cpf = cpf
        )
        cliente.save()
        for carro, placa, ano in zip(carros, placas, anos):
            car = Carro(carro=carro, placa=placa, ano=ano, cliente=cliente)
            car.save()
            print(carro, placa, ano)
        return HttpResponse('Hello World!')

def att_cliente(request):
    id_cliente = request.POST.get('id_cliente')
    cliente = Cliente.objects.filter(id=id_cliente)
    carros = Carro.objects.filter(cliente=cliente[0])

    clientes_json = json.loads(serializers.serialize('json', cliente))[0]['fields']
    #lista de dados
    carros_json = json.loads(serializers.serialize('json', carros))
    carros_json = [ {'fields': carro['fields'], 'id': carro['pk'] } for carro in carros_json]
    data = {'cliente': clientes_json, 'carros': carros_json}
    print(data)
    return JsonResponse(data)
