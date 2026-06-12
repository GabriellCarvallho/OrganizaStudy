from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        return render(request, 'accounts/login.html', {'error': 'Usuário ou senha incorretos'})
    return render(request, 'accounts/login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request, 'accounts/register.html', {'error': 'As senhas não coincidem'})

        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {'error': 'Usuário já existe'})

        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        return redirect('/dashboard/')

    return render(request, 'accounts/register.html')



@login_required
def dashboard_view(request):
    return render(request, 'dashboard/index.html')
    
