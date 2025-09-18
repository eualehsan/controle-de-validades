from django.shortcuts import render, redirect, get_object_or_404
from .models import Marca

def lista_marcas(request):
    marcas = Marca.objects.all()
    return render(request, 'lista_marcas.html', {'marcas':marcas})

def cadastra_marca(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        marca = Marca(nome=nome)
        marca.save()
        return redirect('lista_marcas')
    return render(request, 'cadastrar_marca.html')

def atualiza_marca(request, id):
    if request.method == 'GET':
        marca = get_object_or_404(Marca, id=id)
        return render(request, 'cadastra_marca.html', {'marca': marca})
    
    if request.method == 'POST':
        marca = get_object_or_404(Marca, id=id)

        nome = request.POST.get('nome')

        marca.nome = nome
        marca.save()
        return redirect('lista_marcas')
    return render(request, 'atualiza_marca.html')

def deleta_marca(request, id):
    marca = get_object_or_404(Marca, id=id)

    marca.delete()
    return redirect('lista_marcas')
