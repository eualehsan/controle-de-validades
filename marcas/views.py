from django.shortcuts import render, redirect, get_object_or_404
from .models import Marca
from django.contrib.auth.decorators import login_required

@login_required(login_url='loga_usuario')
def lista_marcas(request):
    marcas = Marca.objects.all()
    return render(request, 'lista_marcas.html', {'marcas':marcas})

@login_required
def cadastra_marca(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        marca = Marca(nome=nome)
        marca.save()
        return redirect('lista_marcas')
    return render(request, 'cadastrar_marca.html')

@login_required
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

@login_required
def deleta_marca(request, id):
    marca = get_object_or_404(Marca, id=id)

    marca.delete()
    return redirect('lista_marcas')
