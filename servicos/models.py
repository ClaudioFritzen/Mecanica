from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from clientes.models import Cliente

# Create your models here.
class Servico(models.Model):
    titulo = models.CharField(_MAX_LENGTH=30)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null = True)

    data_inicio = models.DateField(null=True)
    date_entrega = models.DateField(null=True)
    finalizado = models.BooleanField(default=True)

    #protocolo de serviço
    protocolo = models.CharField(max_length=32, null=True, blank=True)
