from django.views.generic import TemplateView

# Create your views here.
class IndexAlunos(TemplateView):
    template_name = 'paginas/index_aluno.html'

class CadastrarAluno(TemplateView):
    template_name = 'paginas/cadastrar_aluno.html'

class AlterarAluno(TemplateView):
    template_name = 'paginas/alterar_aluno.html'
