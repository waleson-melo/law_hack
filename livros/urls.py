from django.urls import path

from .views import *


urlpatterns = [
    path('', IndexLivro.as_view(), name='livros-index'),
    path('cadastrar/', CadastrarLivro.as_view(), name='livros-cadastrar'),
    path('alterar/', AlterarLivro.as_view(), name='livros-alterar'),
    path('listar-livros/', ListarLivros.as_view(), name='livros-listar'),
]
