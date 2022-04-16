from django.urls import path

from .views import *


urlpatterns = [
    path('', IndexAlunos.as_view(), name='index_aluno'),
    path('cadastrar/', CadastrarAluno.as_view(), name='cadastrar_aluno'),
    path('alterar/<int:pk>/', AlterarAluno.as_view(), name='alterar_aluno'),
    path('listar-alunos/', ListarAlunos.as_view(), name='listar_alunos'),
]
