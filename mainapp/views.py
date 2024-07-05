from django.shortcuts import render
from django.contrib.auth import authenticate, login as logIn, logout
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    print (request.user)
    if request.user.is_authenticated:
        return render(request, 'mainapp/index.html', {
            'title': 'Inicio',
            'breadcrumb': [],
            # 'data': categories
        })
    else:
        return redirect('login')
        

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print (user)
        if (user is not None):
            logIn(request, user)
            return redirect('index')
        else:
            messages.warning(request, 'Usuario o contraseña invalidas')
    
    return render(request, 'mainapp/login.html',{
        'title':'Login'
    })

def logout_user(request):
    logout(request)
    return redirect('index')