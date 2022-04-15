from django.views.generic import TemplateView

# Create your views here.
class IndexLivro(TemplateView):
    template_name = 'paginas/index_livro.html'

class CadastrarLivro(TemplateView):
    template_name = 'paginas/cadastrar_livro.html'

class AlterarLivro(TemplateView):
    template_name = 'paginas/alterar_livro.html'

class ListarLivros(TemplateView):
    template_name = 'paginas/listar_livros.html'
