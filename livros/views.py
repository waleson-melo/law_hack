from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


# Create your views here.
class IndexLivro(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('usuarios-login')
    template_name = 'paginas/index_livro.html'

class CadastrarLivro(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('usuarios-login')
    template_name = 'paginas/cadastrar_livro.html'

class AlterarLivro(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('usuarios-login')
    template_name = 'paginas/alterar_livro.html'

class ListarLivros(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('usuarios-login')
    template_name = 'paginas/listar_livros.html'
