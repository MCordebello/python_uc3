from django.db import models
from django.contrib.auth.models import AbstractUser 

class Perfil(models.Model):
   
    user = models.OneToOneField(
        'auth.User', 
        on_delete=models.CASCADE,
        related_name='perfil'
    )
    foto = models.ImageField(upload_to='perfil_fotos/', blank=True, null=True)
    cpf = models.CharField(max_length=14, unique=True)
    tel_fixo = models.CharField(max_length=15, blank=True, null=True)
    tel_celular = models.CharField(max_length=15)
    dt_nascimento = models.DateField(blank=True, null=True)
    genero = models.CharField(max_length=50, blank=True, null=True)
    desafio_pergunta = models.CharField(max_length=255)
    desafio_resposta = models.CharField(max_length=255)

    def __str__(self):
        return f'Perfil de {self.user.username}'

class Endereco(models.Model):
   
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='enderecos'
    )
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.logradouro}, {self.numero} - {self.cidade}'