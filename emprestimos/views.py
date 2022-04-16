from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


# Create your views here.
class IndexEmprestimo(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('usuarios-login')
    template_name = 'paginas/index_emprestimo.html'

class CadastrarEmprestimo(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('usuarios-login')
    template_name = 'paginas/cadastrar_emprestimo.html'

class ListarEmprestimos(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('usuarios-login')
    template_name = 'paginas/listar_emprestimos.html'
