from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario
from django import forms

class UsuarioRegistrationForm(UserCreationForm):
    
    cpf = forms.CharField(max_length=11, label="CPF", required=True)
    phone = forms.CharField(max_length=11, label="Telefone")
    cep = forms.CharField(max_length=9, required=True, label="CEP")
    first_name = forms.CharField(max_length=30, label="Nome", required=True)
    last_name = forms.CharField(max_length=30, label="Sobrenome", required=True)
    
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'first_name', 'last_name', 'cpf', 'phone', 'cep', 'password1', 'password2')
