from django.urls import path

from .views import *


urlpatterns = [
    path('', IndexUsuarios.as_view(), name='usuarios-index'),
    path('cadastrar/', CadastrarUsuario.as_view(), name='usuarios-cadastrar'),
    path('alterar/', AlterarUsuario.as_view(), name='usuarios-alterar'),
    path('listar-usuarios/', ListarUsuarios.as_view(), name='usuarios-listar'),
]
