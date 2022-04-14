from django.views.generic import TemplateView

# Create your views here.
class IndexUsuarios(TemplateView):
    template_name = 'paginas/index_usuario.html'

class CadastrarUsuario(TemplateView):
    template_name = 'paginas/cadastrar_usuario.html'

class AlterarUsuario(TemplateView):
    template_name = 'paginas/alterar_usuario.html'

class ListarUsuarios(TemplateView):
    template_name = 'paginas/listar_usuarios.html'
