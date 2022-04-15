from django.urls import path

from .views import *


urlpatterns = [
    path('', IndexEmprestimo.as_view(), name='emprestimos-index'),
    path('cadastrar/', CadastrarEmprestimo.as_view(), name='emprestimos-cadastrar'),
    path('listar-emprestimos/', ListarEmprestimos.as_view(), name='emprestimos-listar'),
]
