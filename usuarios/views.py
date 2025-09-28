from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def cadastra_usuario(request):
    if request.method == 'GET':
        return render(request, 'cadastra_usuario.html')
    else:
        usuario = request.POST.get('usuario')
        usuario = usuario.replace(" ", "")
        nome = request.POST.get('nome')
        nome = nome.strip()
        sobrenome = request.POST.get('sobrenome')
        sobrenome = sobrenome.strip()
        email = request.POST.get('email')
        email = email.replace("", "")
        senha = request.POST.get('senha')
        senha = senha.replace(" ", "")
        confirm_senha = request.POST.get('confirm_senha')
        confirm_senha = confirm_senha.replace(" ", "")

        usuario_existe = User.objects.filter(username=usuario).first()
        if  senha != confirm_senha:
            return HttpResponse("SENHAS NAO COMBINAM!")
        elif usuario_existe:
            return HttpResponse("USUARIO JA CADASTRADO!")
        else:
            novo_usuario = User.objects.create_user(
                username=usuario,
                first_name=nome,
                last_name=sobrenome,
                email=email,
                password=senha
                )
            novo_usuario.save()
            usuario = authenticate(username=usuario, password=senha)
            if usuario:
                login(request, usuario)
                return redirect('carrega_inicio')


def loga_usuario(request):
    if request.method =='GET':
        return render(request, 'login_usuario.html')
    else:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        
        usuario_autenticado = authenticate(username=usuario, password=senha)

        if usuario_autenticado:
            login(request, usuario_autenticado)
            return redirect('carrega_inicio')
        else:
            return HttpResponse("USUARIO OU SENHA INVALIDOS! TENTE NOVAMENTE!")

def logout_usuario(request):
    logout(request)
    return redirect('loga_usuario')
           