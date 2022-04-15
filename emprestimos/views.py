from re import template
from django.views.generic import TemplateView

# Create your views here.
class IndexEmprestimo(TemplateView):
    template_name = 'paginas/index_emprestimo.html'

class CadastrarEmprestimo(TemplateView):
    template_name = 'paginas/cadastrar_emprestimo.html'

class ListarEmprestimos(TemplateView):
    template_name = 'paginas/listar_emprestimos.html'
