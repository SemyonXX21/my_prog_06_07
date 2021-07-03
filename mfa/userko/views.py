from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def user_page(request):
    return render(request, 'user.html')

def register_page(request):
    if request.user.is_authenticated: #только считываемая инфа
        return redirect('base')
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Aккаунт был создан для' + form.cleaned_data.get('username'))
            return redirect('login')

    context = {
        'form': form
    }

    return render(request, 'register.html', context)


def login_page(request):
    if request.user.is_authenticated: #только считываемая инфа
        return redirect('base')
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base')
        else:
            messages.info(request, 'Неверно имя пользователя или пороль!')
    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('login')
