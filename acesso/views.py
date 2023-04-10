from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UsuarioRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UsuarioRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('homepage')
    else:
        form = UsuarioRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})