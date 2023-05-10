from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from .forms import RegisterForm
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from .forms import LoginForm


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return HttpResponse("<h4>about</h4>")


def personal_cabinet_page(request):
    return render(request, 'main/personal_cabinet.html')


def portfolio(request):
    return render(request, 'portfolio/portfolio.html')


def pageNotFound(request, exception):
    return render(request, 'main/404.html', status=404)


# Определяем функцию-представление
class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'main/login.html'
