from django.urls import path
from . import views  # Importa o módulo views do app atual
from .views import obd_diagnostics  # Importa especificamente a função obd_diagnostics da views.py

# Lista de rotas do aplicativo
urlpatterns = [
    # Rota para o endpoint inicial (index), que exibe uma mensagem de status da API
    path('', views.index, name='index'),

    # Rota para o endpoint de diagnóstico OBD-II
    path('obd/', obd_diagnostics, name='obd_diagnostics'),
]
