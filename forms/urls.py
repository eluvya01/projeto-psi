from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:cliente_id>/tela_cliente/', views.tela_cliente, name='tela_cliente'),
    # ex: /polls/5/tela_sessao/
    path('<int:sessao_id>/tela_sessao/', views.tela_sessao, name='tela_sessao'),
]
