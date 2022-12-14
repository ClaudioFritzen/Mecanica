from secrets import token_hex
from django.db import models
from clientes.models import Cliente
from .choices import ChoicesCategoriaManuntencao

# import para pegar a data atual
from datetime import datetime


# Create your models here.
class CategoriaManutencao(models.Model):
    titulo = models.CharField(max_length=3, choices=ChoicesCategoriaManuntencao.choices)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return self.titulo


class Servico(models.Model):
    titulo = models.CharField(max_length=70)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    categoria_manutencao = models.ManyToManyField(CategoriaManutencao)
    data_inicio = models.DateField(null=True)
    date_entrega = models.DateField(null=True)
    finalizado = models.BooleanField(default=True)
    
    #protocolo de serviço
    protocolo = models.CharField(max_length=52, null=True, blank=True)

    def __str__(self) -> str:
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.protocolo:
            self.protocolo = datetime.now().strftime("%d/%m/%Y-%H:%M:%S-") + token_hex(16)
            
        super(Servico, self).save(*args, **kwargs)
    
    def preco_total(self):
        preco_total = float(0)
        for categoria in self.categoria_manutencao.all():
            preco_total += float(categoria.preco)
        return preco_total