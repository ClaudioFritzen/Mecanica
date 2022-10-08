from django.urls import path
from . import views

urlpatterns = [
    path('', views.servicos, name="servicos"),
   # path('atualiza_cliente/', views.att_cliente, name="atualiza_cliente"),
]