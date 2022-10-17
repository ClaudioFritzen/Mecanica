from django.forms import ModelForm
from .models import Servico, CategoriaManutencao

class FormServico(ModelForm):
    class Meta:
        model = Servico
        """
        # trazendo todos os campos em uma linha
        # fields = '__all__'

        #trazendo só os escolhidos
       # fields = ['titulo', 'cliente']

        # "exclude" exclui os campos que quiser nesse caso
        # serão os campos que o usuário não tera
        # contato na hora de criar um novo serviço 
        # o finalizado, quando inicia um serviço ele não tem como ta finalizado
        # e o n° de protocolo que é gerado automaticamente pelo sistema
        """
        exclude  = ['finalizado', 'protocolo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """
            estilizar o html criado pelo django
            pegando uma linha e colocando dentro do css
            self.fields['titulo'].widget.attrs.update({'class': 'form-control'})

            Mas fazer isso pra cada campo seria trabalhoso de mais, e ia ter muito codigo repetido
            entao faremos um "for" e conseguimos atribuir a classe para todos os campos

        """
        for fields in self.fields:
            self.fields[fields].widget.attrs.update({'class': 'form-control'})
            self.fields[fields].widget.attrs.update({'placeholder': fields})

        for i, j in self.fields['categoria_manutencao'].choices:
            print(i,j)
        

