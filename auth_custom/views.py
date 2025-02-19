from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, SignupForm, ProfileForm
from django.contrib.auth import get_user_model

User = get_user_model()

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('dashboard')  # Redireciona para a página inicial
            else:
                messages.error(request, 'E-mail ou senha incorretos.')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = LoginForm()
    return render(request, 'usuarios/login.html', {'login_form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']  # Usa o e-mail como username
            user.save()
            messages.success(request, 'Cadastro realizado com sucesso! Bem-vindo ao Condofácil!')
            return redirect('login')  # Redireciona para a página de login
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = SignupForm()
    return render(request, 'usuarios/login.html', {'signup_form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Você foi desconectado com sucesso.')
    return redirect('login')