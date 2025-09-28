from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from datetime import date
from .models import Validade
from produtos.models import Produto
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def lista_validades(request):
    if request.method == 'GET':
        usuario = request.user
        usuario_id = usuario.id
        usuario_atual = User.objects.get(id=usuario_id)
        validades = Validade.objects.filter(usuario=usuario_atual)
        return render(request, 'lista_validades.html', {'validades': validades})

@login_required
def cadastrar_validade(request):
    produtos = Produto.objects.all().order_by('descricao')
    contexto = {
        'produtos': produtos
    }
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        dt_validade = request.POST.get('dt_validade')
        estoque = request.POST.get('estoque')
        usuario = request.user
        usuario_id = usuario.id

        usuario_atual = User.objects.get(id=usuario_id)
        produto = Produto.objects.get(id=produto_id)

        validade = Validade(
            produto=produto,
            dt_validade=dt_validade,
            estoque=estoque,
            usuario=usuario_atual 
        )
        validade.save()

        return redirect ('lista_validades')
    
    return render(request, 'cadastrar_validade.html', contexto)

@login_required
def edita_validade(request, id):
    if request.method == 'GET':
        validade = get_object_or_404(Validade, id=id)
        return render(request, 'cadastra_validade.html', {'validade':validade})

    if request.method == 'POST':
        validade = get_object_or_404(Validade, id=id, usuario=request.user)
        if validade:
            estoque = request.POST.get('estoque')
            validade.estoque = estoque
            validade.save()
            return redirect('lista_validades')
        else:
            return HttpResponse("ERRO AO EDITAR VALIDADE")
        
@login_required    
def deleta_validade(request, id):
    validade = get_object_or_404(Validade, id=id, usuario=request.user)
    
    validade.delete()
    return redirect('lista_validades')