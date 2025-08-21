from django.db import models

# Categoria
class Category(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

# Produto
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)
    quantidade = models.PositiveIntegerField(default=0)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    status = models.BooleanField(default=True)
    
    # Campos de data
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    # Relacionamento com categoria
    Tipo = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="produtos"
    )

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
