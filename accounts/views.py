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
        return redirect('/login/')

    return render(request, 'accounts/register.html')



@login_required
def dashboard_view(request):
    return render(request, 'dashboard/index.html')


@login_required
def subjects_view(request):
    return render(request, 'subjects/index.html')


    
@login_required
def tarefas_view(request):
    return render(request, 'tarefas/index.html')




@login_required
def revisao_view(request):
    return render(request, 'revisao/index.html')




@login_required
def estatisticas_view(request):
    return render(request, 'estatisticas/index.html')



@login_required
def assistente_view(request):
    return render(request, 'assistente/index.html')


@login_required
def configuracoes_view(request):
    return render(request, 'configuracoes/index.html')



@login_required
def metas_view(request):
    return render(request, 'metas/index.html')



@login_required
def cronograma_view(request):
    return render(request, 'cronograma/index.html')