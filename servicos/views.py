from django.shortcuts import render
from django.http import HttpResponse

# 
from .forms import FormServico

# Create your views here.
def novo_servico(request):
    #return HttpResponse('Hello World!')
       
    if request.method == "GET":
        form = FormServico()
        return render(request, 'novo_servico.html', {'form': form}) 
    elif request.method == "POST":
        form = FormServico(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('Dados salvo com sucesso')

        else:
            return render(request, 'novo_servico.html', {'form': form})
     