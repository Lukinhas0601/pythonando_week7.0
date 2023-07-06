from django.shortcuts import render
from perfil.models import Categoria, Conta


def novo_valor(request):
    if request.method == 'GET':
        contas = Conta.objects.all()
        categoria = Categoria.objects.all()

        return render(request, 'novo_valor.html', {'contas' : contas, 'categoria' : categoria})
