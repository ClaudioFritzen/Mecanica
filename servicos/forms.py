from django.forms import ModelForm
from .models import Servico, CategoriaManutencao

class FormServico(ModelForm):
    class Meta:
        model = Servico
        # trazendo todos os campos em uma linha
        # fields = '__all__'

        #trazendo só os escolhidos
       # fields = ['titulo', 'cliente']

        # "exclude" exclui os campos que quiser nesse caso
        # serão os campos que o usuário não tera
        # contato na hora de criar um novo serviço 
        # o finalizado, quando inicia um serviço ele não tem como ta finalizado
        # e o n° de protocolo que é gerado automaticamente pelo sistema
        exclude  = ['finalizado', 'protocolo']

