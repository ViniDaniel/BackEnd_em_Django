from django.shortcuts import render
from .models import Fornecedor

# Create your views here.

def home(request):
    return render(request, "fornecedores/home.html")

def fornecedores(request):
    #salvando dados no banco de dados
    novo_fornecedor = Fornecedor()
    novo_fornecedor.nome = request.POST.get('nome')
    novo_fornecedor.cnpj = request.POST.get('cnpj')
    novo_fornecedor.endereco = request.POST.get('endereco')
    novo_fornecedor.celular = request.POST.get('celular')
    novo_fornecedor.email = request.POST.get('email')
    novo_fornecedor.produto = request.POST.get('produto')
    novo_fornecedor.save()
    #mostrando em nova pagina
    fornecedores = {
        'fornecedores': Fornecedor.objects.all()
    }
    #retornar os dados
    return render(request, 'fornecedores/perfil.html',fornecedores)