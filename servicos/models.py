from django.db import models
from clientes.models import Cliente
from servicos.choices import ChoicesCcategoriaManuntencao

# Create your models here.
class Servico(models.Model):
    titulo = models.CharField(max_length=30)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null = True)

    data_inicio = models.DateField(null=True)
    date_entrega = models.DateField(null=True)
    finalizado = models.BooleanField(default=True)

    #protocolo de serviço
    protocolo = models.CharField(max_length=32, null=True, blank=True)

class CategoriaManutencao(models.Model):
    titulo = models.CharField(max_length=3, choices=ChoicesCcategoriaManuntencao.choices)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return self.titulo
