from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy


# Create your views here.
class IndexUsuarios(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('usuarios-login')
    group_required = u'Administrador'
    template_name = 'paginas/index_usuario.html'


class CadastrarUsuario(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('usuarios-login')
    group_required = u'Administrador'
    template_name = 'paginas/cadastrar_usuario.html'


class AlterarUsuario(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('usuarios-login')
    group_required = u'Administrador'
    template_name = 'paginas/alterar_usuario.html'


class ListarUsuarios(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('usuarios-login')
    group_required = u'Administrador'
    template_name = 'paginas/listar_usuarios.html'
