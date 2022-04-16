from django.db import models


# Create your models here.
class Aluno(models.Model):
    cpf = models.CharField(max_length=11, unique=True, verbose_name='CPF')
    matricula = models.CharField(max_length=8, unique=True)
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=50, verbose_name='Endereço')
    status_pendencia = models.BooleanField(default=False)
    status_ativo = models.BooleanField(default=True)

    def __str__(self):
        return 'Mat.: {}, Nome: {}, Status Pendência: {}, Ativo: {}'.format(
            self.matricula, self.nome, self.status_pendencia, self.status_ativo
        )
