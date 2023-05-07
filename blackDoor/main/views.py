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
def register(request):
    # Если запрос был отправлен методом POST (в форме была нажата кнопка "Отправить")
    if request.method == 'POST':
        # Создаем форму, используя данные из POST-запроса
        form = RegisterForm(request.POST)
        # Проверяем, прошла ли форма валидацию
        if form.is_valid():
            # Создаем нового пользователя, не сохраняя его в базе данных
            user = form.save(commit=False)
            # Сохраняем пользователя в базе данных
            user.save()
            # Перенаправляем пользователя на домашнюю страницу
            return redirect('home')
    # Если запрос был отправлен методом GET (просто открыли страницу с формой)
    else:
        # Создаем пустую форму
        form = RegisterForm()
    # Рендерим шаблон с формой регистрации и передаем в него форму
    return render(request, 'main/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        try:
            user = authenticate(request, email=email, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = 'Invalid email or password'
                return render(request, 'main/login.html', {'message': message})
        except Exception as e:
            message = str(e)
            return render(request, 'main/login.html', {'message': message})
    else:
        return render(request, 'main/login.html')
