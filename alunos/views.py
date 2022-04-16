from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import Aluno


# Create your views here.
class IndexAlunos(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('usuarios-login')
    template_name = 'paginas/index_aluno.html'


class CadastrarAluno(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('usuarios-login')
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('cadastrar_aluno')
    model = Aluno
    fields = [
        'cpf',
        'matricula',
        'nome',
        'email',
        'telefone',
        'endereco',
    ]

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Cadastrar Aluno'

        return context


class AlterarAluno(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('usuarios-login')
    template_name = 'paginas/form.html'
    success_url = reverse_lazy('cadastrar_aluno')
    model = Aluno
    fields = [
        'cpf',
        'matricula',
        'nome',
        'email',
        'telefone',
        'endereco',
    ]

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Alterar Aluno'

        return context


class ListarAlunos(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('usuarios-login')
    template_name = 'paginas/listar_alunos.html'
    model = Aluno
