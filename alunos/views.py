from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import Aluno


# Create your views here.
class IndexAlunos(TemplateView):
    template_name = 'paginas/index_aluno.html'


class CadastrarAluno(CreateView):
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


class AlterarAluno(UpdateView):
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


class ListarAlunos(ListView):
    template_name = 'paginas/listar_alunos.html'
    model = Aluno
