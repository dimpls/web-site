from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return HttpResponse("<h4>about</h4>")

def personal_cabinet_page(request):
    return render(request, 'main/personal_cabinet.html')

def portfolio(request):
    return render(request, 'portfolio/portfolio.html')
