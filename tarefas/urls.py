from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #path('jogadores/', views.jogadores, name='jogadores'),
    path('jogadores/', views.lista_jogadores, name='lista_jogadores'),
    path('criar_jogador/', views.criar_jogador, name='criar_jogador'),
    path('detalhe_jogador/<int:pk>/', views.detalhe_jogador, name='detalhe_jogador'),
    path('editar_jogador/<int:pk>/', views.editar_jogador, name='editar_jogador'),
    path('excluir_jogador/<int:pk>/', views.excluir_jogador, name='excluir_jogador'),
    path('sobre/', views.sobre, name='sobre'),
]