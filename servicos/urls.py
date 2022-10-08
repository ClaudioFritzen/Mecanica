from django.urls import path
from . import views

urlpatterns = [
    path('novo_servico', views.novo_servico, name="novo_servico"),
   # path('atualiza_cliente/', views.att_cliente, name="atualiza_cliente"),
]