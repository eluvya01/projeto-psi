from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Cliente
from .models import Sessoes
from django.shortcuts import get_object_or_404, render

'''def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
'''
def index(request):
    latest_cliente_list = Cliente.objects.all()
    template = loader.get_template('forms/index.html')
    context = {
        'latest_cliente_list': latest_cliente_list,
    }
    return HttpResponse(template.render(context, request))

def tela_cliente(request,cliente_id):
    return HttpResponse("Cadastro de Cliente")

def tela_sessao(request,sessao_id):
    return HttpResponse("Cadastro de Sessão")

# get_object_or_404()
def detail(request, cliente_id):
    question = get_object_or_404(Cliente, pk=cliente_id)
    return render(request, 'forms/cliente.html', {'cliente': cliente})

def detail(request, sessao_id):
    question = get_object_or_404(Sessao, pk=sessao_id)
    return render(request, 'forms/sessao.html', {'sessao': sessao})
