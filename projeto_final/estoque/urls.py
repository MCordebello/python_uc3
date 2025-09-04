from django.urls import path
from . import views 

urlpatterns = [

    path('', views.lista_produtos, name='lista_produtos'),

    
    path('<int:pk>/', views.detalhe_produto, name='detalhe_produto'),
]