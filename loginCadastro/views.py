from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.models import User
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        email_user = request.POST.get('email')
        password_user = request.POST.get('password')
        print(f'email == {email_user}\npassword == {password_user}')

    if User.objects.filter(email=email_user).exists():
        nome = User.objects.filter(email=email_user).values_list('username', flat=True).get()
        user = authenticate(username=nome, password=password_user )
        if user:
            print("autenticado")
            login_django(request, user)
        else:
            print("Email ou senha incorretos")
        print(f" resultado do user: {user} \nresultado do nome: {nome}")
    else:
        print("Email ou senha incorretos")

    return render(request, 'tela-login.html')