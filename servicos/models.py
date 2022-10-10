from django.db import models
from clientes.models import Cliente
from .choices import ChoicesCategoriaManuntencao


# Create your models here.
class CategoriaManutencao(models.Model):
    titulo = models.CharField(max_length=3, choices=ChoicesCategoriaManuntencao.choices)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return self.titulo


class Servico(models.Model):
    titulo = models.CharField(max_length=30)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null = True)
    categoria_manutencao = models.ManyToManyField(CategoriaManutencao)
    data_inicio = models.DateField(null=True)
    date_entrega = models.DateField(null=True)
    finalizado = models.BooleanField(default=True)

    #protocolo de serviço
    protocolo = models.CharField(max_length=32, null=True, blank=True)

