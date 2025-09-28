from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Produto
from categorias.models import Categoria
from marcas.models import Marca
from django.contrib.auth.decorators import login_required

@login_required
def exibe_erro(request):
     return render(request, 'erro.html')

@login_required(login_url='loga_usuario')
def carrega_inicio(request):
     usuario = request.user
     return render(request, 'index.html', {'usuario':usuario})

@login_required(login_url='loga_usuario')
def lista_produtos(request):
    categorias = Categoria.objects.all()
    marcas = Marca.objects.all()
    produtos = Produto.objects.all()

    contexto = {
        'categorias': categorias,
        'marcas': marcas,
        'produtos': produtos
    }
    
    return render(request, 'lista_produtos.html', contexto)
    
@login_required
def cadastrar_produto(request):
    categorias = Categoria.objects.all()
    marcas = Marca.objects.all()

    contexto = {
            'categorias': categorias,
            'marcas': marcas
    }

    if request.method == 'POST':
        cod_barras = request.POST.get('codigo_de_barras')
        descricao = request.POST.get('descricao')
        categoria_id = request.POST.get('categoria')
        marca_id = request.POST.get('marca')
        criado_por = request.user

        categoria = Categoria.objects.get(id=categoria_id)
        marca = Marca.objects.get(id=marca_id)

        produto = Produto(
            codigo_barras=cod_barras,
            descricao=descricao,
            categoria=categoria,
            marca=marca,
            criado_por=criado_por
        )
        produto.save()

        return redirect('lista_produtos')
    return render(request, 'cadastrar_produto.html', contexto)

@login_required
def edita_produto(request, id):
    if request.method == 'GET': 
        produto = get_object_or_404(Produto, id=id)
        return render(request, 'cadastrar_produto.html', {'produto': produto})
    
    if request.method == 'POST':
        produto = get_object_or_404(Produto, id=id)

        cod_barras = request.POST.get('codigo de barras')
        descricao = request.POST.get('descricao')
        categoria_id = request.POST.get('categoria')
        marca_id = request.POST.get('marca')

        categoria = Categoria.objects.get(id=categoria_id)
        marca = Marca.objects.get(id=marca_id)
     
        produto.codigo_barras = cod_barras
        produto.descricao = descricao
        produto.categoria = categoria
        produto.marca = marca
        produto.save()
        
        return redirect('lista_produtos')
    return render(request, 'edita_produto.html')

@login_required
def deleta_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('lista_produtos')

@login_required
def deleta_todos_produtos(request):
    if request.method == 'GET':
        produtos = Produto.objects.all()
        produtos.delete()
        return render(request, 'lista_produtos.html')
     