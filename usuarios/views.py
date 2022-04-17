from unicodedata import name
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from .forms import UsuarioForm


# Create your views here.
class IndexUsuarios(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('usuarios-login')
    group_required = u'Administrador'
    template_name = 'paginas/index_usuario.html'


class CadastrarUsuario(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('usuarios-login')
    group_required = u'Administrador'
    template_name = 'usuarios/form.html'
    success_url = reverse_lazy('usuarios-listar')
    form_class = UsuarioForm

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name='Bibliotecario')

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Cadastrar Usuário'

        return context


class AlterarUsuario(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('usuarios-login')
    group_required = u'Administrador'
    template_name = 'paginas/alterar_usuario.html'


class ListarUsuarios(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('usuarios-login')
    group_required = u'Administrador'
    template_name = 'paginas/listar_usuarios.html'
