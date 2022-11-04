import re
from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Cliente, Carro

from django.core import serializers
import json

from django.views.decorators.csrf import csrf_exempt

# importações para fazer o try de excluir
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404

# imports para mensagens personalizadas
from django.contrib.messages import constants
from django.contrib import messages

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
        print(nome, sobrenome,email, cpf)
        # se tiver faz
        if cliente.exists():
            messages.add_message(request, constants.ERROR, 'CPF já existente')
            return render(request, 'clientes.html', {'nome': nome, 'sobrenome': sobrenome, 'email': email, 'carros': zip(carros, placas, anos)})
           
        email = Cliente.objects.filter(email=email)
        messages.add_message(request, constants.ERROR, 'Email já existente')
        # validação do email
        #if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
         #   messages.add_message(request, constants.ERROR, 'Email inválido!')
        return render(request,'clientes.html', {'nome': nome, 'sobrenome': sobrenome, 'cpf': cpf, 'carros': zip(carros, placas, anos)})
           



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
    cliente_id = json.loads(serializers.serialize('json', cliente))[0]['pk']
    
    #lista de dados
    carros_json = json.loads(serializers.serialize('json', carros))
    carros_json = [ {'fields': carro['fields'], 'id': carro['pk'] } for carro in carros_json]
    data = {'cliente': clientes_json, 'carros': carros_json, 'cliente_id': cliente_id}
    
    return JsonResponse(data)

@csrf_exempt
def update_carro(request, id):
    nome_carro = request.POST.get('carro')
    placa = request.POST.get('placa')
    ano = request.POST.get('ano')

    carro = Carro.objects.get(id=id)
    list_carros = Carro.objects.filter(placa=placa).exclude(id=id)
    if list_carros.exists():
        return HttpResponse('Hello World! Carro já existe')

    # salvando no banco quando os dados dos carros forem alterados

    carro.carro = nome_carro
    carro.placa = placa
    carro.ano = ano 
    carro.save()

    return HttpResponse('Hello World! Itens alterados com sucesso!')

def excluir_carro(request, id):
    try:
        carro = Carro.objects.get(id=id)
        carro.delete()
        return redirect(reverse('clientes')+f'?aba=att_cliente&id_cliente={id}')
    except:
        #todo exibir mms de erro
        return redirect(reverse('clientes')+f'?aba=att_cliente&id_cliente={id}')

def update_cliente(request, id):
    body = json.loads(request.body)
    nome = body['nome']
    sobrenome = body['sobrenome']
    email = body['email']
    cpf = body['cpf']


    cliente = get_object_or_404(Cliente, id=id)
    
    try:
        cliente.nome = nome
        cliente.sobrenome = sobrenome
        cliente.email = email
        cliente.cpf = cpf
        cliente.save()
        return JsonResponse({'status': '200', 'nome': nome, 'sobrenome': sobrenome, 'email': email, 'cpf': cpf})
    except:

        return JsonResponse({'status': 500})
    