from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='usuarios/login.html'
    ), name='usuarios-login'),
    path('logout/', auth_views.LogoutView.as_view(), name='usuarios-logout'),
    path('administrador/', IndexUsuarios.as_view(), name='usuarios-index'),
    path('administrador/cadastrar/', CadastrarUsuario.as_view(), name='usuarios-cadastrar'),
    path('administrador/alterar/', AlterarUsuario.as_view(), name='usuarios-alterar'),
    path('administrador/listar-usuarios/', ListarUsuarios.as_view(), name='usuarios-listar'),
]
