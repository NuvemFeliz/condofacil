from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

class LoginForm(forms.Form):
    email = forms.EmailField(label="E-mail", widget=forms.EmailInput(attrs={
        'placeholder': 'E-mail',
        'required': True,
    }))
    password = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={
        'placeholder': 'Senha',
        'required': True,
    }))

class SignupForm(UserCreationForm):
    full_name = forms.CharField(label="Nome completo", widget=forms.TextInput(attrs={
        'placeholder': 'Nome completo',
        'required': True,
    }))
    telefone = forms.CharField(label="Telefone", widget=forms.TextInput(attrs={
        'placeholder': 'Telefone',
        'required': True,
    }))
    nif = forms.CharField(label="NIF", widget=forms.TextInput(attrs={
        'placeholder': 'NIF',
        'required': True,
    }))
    data_nascimento = forms.DateField(label="Data de Nascimento", widget=forms.DateInput(attrs={
        'type': 'date',
        'required': True,
    }))

    class Meta:
        model = User
        fields = ['full_name', 'email', 'telefone', 'nif', 'data_nascimento', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['foto_perfil', 'endereco']