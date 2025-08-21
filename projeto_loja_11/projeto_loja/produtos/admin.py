# produtos/admin.py - Aula 11

from django.contrib import admin
from.models import Produto # <-- Importa o modelo Produto da sua aplicação (Aula 11)

# produtos/admin.py


# Registra o modelo Produto
#admin.site.register(Produto)

# Registra o modelo Produto - Aula 11 parte 01

#admin.site.register(Produto)

# Define uma classe ModelAdmin para o modelo Produto (Aula 11)
class ProdutoAdmin(admin.ModelAdmin):
    
    # Campos que serão exibidos na página de lista de objetos
    list_display = ('nome', 'preco', 'estoque', 'quantidade','status')
    
    # Campos que podem ser clicados para ordenar a lista
    list_display_links = ('nome',)
    
    # Adiciona uma barra lateral de filtro para os campos
    list_filter = ('quantidade', 'data_criacao','status') # Supondo que você tenha um campo data_criacao
    
    # Adiciona uma barra de pesquisa
    search_fields = ('nome', 'descricao') # Pesquisa por nome ou descrição
    
    # Permite editar campos diretamente na lista (cuidado com isso em produção!)
    list_editable = ('preco', 'quantidade','status')
    
    # Pre-popula o campo 'slug' (se você tiver um) baseado no 'nome'
    # prepopulated_fields = {'slug': ('nome',)}
    
    # Agrupa campos no formulário de edição/criação
    fieldsets = (
        (None, {
            'fields': ('nome', 'descricao', 'preco', 'quantidade', 'imagem', 'status')
        }),
    )

# Registra o modelo Produto com a sua classe ModelAdmin personalizada
admin.site.register(Produto)


