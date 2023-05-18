from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
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
from .models import Sketch


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return HttpResponse("<h4>about</h4>")


def personal_cabinet_page(request):
    return render(request, 'main/personal_cabinet.html')


def portfolio(request):
    return render(request, 'portfolio/portfolio.html')


def sketch(request):
    sketches = Sketch.objects.all()
    return render(request, 'main/sketch.html', {'sketches': sketches})


def add_sketches(request):
    # Предположим, у вас есть список путей к фотографиям, которые вы хотите добавить
    photo_paths = ['main/static/main/img/tatto1.png', 'main/static/main/img/tatto2.png', 'main/static/main/img/tatto3.png', 'main/static/main/img/tatto4.png', 'main/static/main/img/tatto5.png',
                   'main/static/main/img/tatto6.png', 'main/static/main/img/tatto7.png', 'main/static/main/img/tatto8.png', 'main/static/main/img/tatto9.png', 'main/static/main/img/tatto10.png',
                   'main/static/main/img/tatto11.png', 'main/static/main/img/tatto12.png', 'main/static/main/img/tatto13.png', 'main/static/main/img/tatto14.png', 'main/static/main/img/tatto15.png',
                   'main/static/main/img/tatto16.png', 'main/static/main/img/tatto17.png']

    tmp = 1000.0
    k = 1
    for path in photo_paths:
        # Создаем новый объект Sketch и сохраняем фотографию
        sketch = Sketch()
        sketch.price = 10
        sketch.photo.save('tatto' + str(k) + '.png', open(path, 'rb'))
        # Заполняем поле 'price' текущим значением price_temp
        #sketch.price = 10.0
        sketch.price = tmp
        tmp += 1200.0
        k += 1
        # Сохраняем объект Sketch в базу данных
        sketch.save()



    return redirect('home')


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


def logout_user(request):
    logout(request)
    return redirect('home')
