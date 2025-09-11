# estoque/views.py

from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    """
    Renders the homepage.
    """
    return render(request, 'home.html')

def index(request):
    """
    Renders the product list page.
    """
    return HttpResponse("<h1>This is the product list page (index).</h1>")

# Existing views (if they exist)
def lista_produtos(request):
    return HttpResponse("<h1>Lista de Produtos.</h1>")

def detalhe_produto(request, pk):
    return HttpResponse(f"<h1>Detalhes do produto {pk}.</h1>")