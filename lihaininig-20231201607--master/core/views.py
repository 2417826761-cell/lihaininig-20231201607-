from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from django.views import View

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'core/register.html', {'form': form})
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, 'core/register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'core/login.html', {'form': form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        return render(request, 'core/login.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'core/profile.html')
