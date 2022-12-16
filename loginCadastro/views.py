from django.shortcuts import render
# from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        email_user = request.POST.get('email')
        password_user = request.POST.get('password')
        print(f'email == {email_user}\npassword == {password_user}')
    return render(request, 'tela-login.html')