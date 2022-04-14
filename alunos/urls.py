from django.urls import path

from .views import IndexAlunos


urlpatterns = [
    path('', IndexAlunos.as_view(), name='index_aluno'),
]
