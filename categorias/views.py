from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'lista_categorias.html', {'categorias': categorias})

def cadastrar_categoria(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        categoria = Categoria(nome=nome)
        categoria.save()
        return redirect('lista_categorias')
    return render(request, 'cadastrar_categoria.html')

def editar_categoria(request, id):
    if request.method == 'GET':
        categoria = get_object_or_404(Categoria, id=id)
        return render(request, 'cadastrar_categorias.html', {'categoria':categoria})
    
    if request.method == 'POST':
        categoria = get_object_or_404(Categoria, id=id)

        nome = request.POST.get('nome')

        categoria.nome = nome
        categoria.save()

        return redirect('lista_categorias')
    return render(request, 'editar_categoria.html')

def deleta_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    return redirect('lista_categorias')
