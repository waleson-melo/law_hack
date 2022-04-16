from django.db import models


# Create your models here.
class Usuario(models.Model):
    ADMINISTRADOR = 0
    BIBLIOTECARIO = 1
    TIPO_USUARIO = [
        (ADMINISTRADOR, 'Administrador'),
        (BIBLIOTECARIO, 'Bibliotecario'),
    ]

    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    usuario = models.CharField(max_length=20, verbose_name='Usuário')
    senha = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11, verbose_name='CPF')
    endereco = models.CharField(max_length=50, verbose_name='Enderço')
    telefone = models.CharField(max_length=11)
    nivel = models.SmallIntegerField(choices=TIPO_USUARIO,
        default=BIBLIOTECARIO, verbose_name='Nível de Acesso')
    status_ativo = models.BooleanField(default=True)

    def __str__(self):
        return 'Nome.: {}, Usuário: {}, Nivel de Acesso: {}, Ativo: {}'.format(
            self.nome, self.usuario, self.nivel, self.status_ativo
        )
