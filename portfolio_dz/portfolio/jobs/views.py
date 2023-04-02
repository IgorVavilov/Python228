from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import Jobs
from django.contrib.auth.decorators import login_required

def index(request):
    jobs = Jobs.objects.all()
    return render(request, 'jobs/index.html', {'jobs': jobs})

def loginuser(request):
    if request.method == "GET":
        return render(request, 'jobs/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'jobs/loginuser.html', {'form': AuthenticationForm(),
                                                           'error': 'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('index')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'jobs/signupuser.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'jobs/signupuser.html', {
                    'form': UserCreationForm(),
                    'error': 'Такое имя пользователя уже существует. Задайте другое.'})

        else:
            return render(request, 'jobs/signupuser.html', {'form': UserCreationForm(),
                                                             'error': 'Пароли не совпадают.'})


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')

