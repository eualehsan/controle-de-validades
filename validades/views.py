from django.shortcuts import render, redirect, get_object_or_404
from datetime import date
from .models import Validade
from produtos.models import Produto

def lista_validades(request):
    if request.method == 'GET':
        validades = Validade.objects.all().order_by('dt_validade')
        return render(request, 'lista_validades.html', {'validades': validades})

def cadastrar_validade(request):
    produtos = Produto.objects.all().order_by('descricao')
    contexto = {
        'produtos': produtos
    }
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        dt_validade = request.POST.get('dt_validade')
        estoque = request.POST.get('estoque')

        produto = Produto.objects.get(id=produto_id)

        validade = Validade(
            produto=produto,
            dt_validade=dt_validade,
            estoque=estoque 
        )
        validade.save()

        return redirect ('lista_validades')
    
    return render(request, 'cadastrar_validade.html', contexto)

def edita_validade(request, id):
    if request.method == 'GET':
        validade = get_object_or_404(Validade, id=id)
        return render(request, 'cadastra_validade.html', {'validade':validade})

    if request.method == 'POST':
        validade = get_object_or_404(Validade, id=id)
        estoque = request.POST.get('estoque')
        validade.estoque = estoque
        validade.save()
        return redirect('lista_validades')
    
def deleta_validade(request, id):
    validade = get_object_or_404(Validade, id=id)
    validade.delete()
    return redirect('lista_validades')
