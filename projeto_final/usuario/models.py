from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(default='perfil_padrao.jpg', upload_to='imagens_perfil')
    nome = models.CharField(max_length=150, verbose_name="Nome")
    email = models.EmailField(verbose_name="E-mail")
    cpf = models.CharField(max_length=11, verbose_name="CPF")
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    telefone_fixo = models.CharField(max_length=10, verbose_name="Telefone 1")
    telefone_celular = models.CharField(max_length=11, verbose_name="Telefone 2")

    def __str__(self):
        return f'Perfil de {self.usuario.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.foto.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.foto.path)


class Genero(models.Model):
    class GeneroChoices(models.TextChoices):
        FEMININO = 'Feminino', 'Feminino'
        MASCULINO = 'Masculino', 'Masculino'
        OUTRO = 'Outro', 'Outro'

    cliente = models.ForeignKey(User, on_delete=models.PROTECT, related_name='genero')
    status = models.CharField(
        max_length=20,
        choices=GeneroChoices.choices,
        default=GeneroChoices.OUTRO
    )

    def __str__(self):
        return f"Gênero de {self.cliente.username}"


class ContactRequest(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Contato de {self.name} - {self.email}"

