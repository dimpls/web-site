from django.core.checks import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

from django.shortcuts import render, redirect
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


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # Перенаправить на страницу входа
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form})
