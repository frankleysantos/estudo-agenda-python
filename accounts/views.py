from unicodedata import name
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    formCadastro = request.POST
    if formCadastro:
        nome = formCadastro.get('nome')
        sobrenome = formCadastro.get('sobrenome')
        email = formCadastro.get('email')
        senha = formCadastro.get('senha')
        repsenha = formCadastro.get('repsenha')
        usuario = formCadastro.get('usuario')
        print(usuario)
        if not nome or not sobrenome or not email or not senha or not repsenha or not usuario:
            messages.add_message(request, messages.ERROR, 'Devem ser preenchidos todos os campos')
            return render(request, 'accounts/register.html')
        
        try:
            validate_email(email)
        except:
            messages.add_message(request, messages.ERROR, 'Campo email é invalido')
            return render(request, 'accounts/register.html')

        if repsenha != senha:
            messages.add_message(request, messages.ERROR, 'Senhas devem ser iguais')
            return render(request, 'accounts/register.html')
        
        if len(senha) <= 6:
            messages.add_message(request, messages.ERROR, 'Senhas deve conter mais 6 caracteres')
            return render(request, 'accounts/register.html')
        
        if User.objects.filter(username=usuario).exists():
            messages.add_message(request, messages.ERROR, 'Usuário já cadastro')
            return render(request, 'accounts/register.html')
        
        if User.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR, 'Email já cadastro')
            return render(request, 'accounts/register.html')

        user = User.objects.create_user(
            username=usuario, 
            email=email, 
            password=senha, 
            first_name=nome, 
            last_name=sobrenome
        )
        user.save()
        messages.add_message(request, messages.SUCCESS, 'Usuário Cadastrado com sucesso. Realize o login')
        return redirect('login')

    return render(request, 'accounts/register.html')

def logout(request):
    return render(request, 'accounts/logout.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
