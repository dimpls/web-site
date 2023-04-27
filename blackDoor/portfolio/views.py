from django.shortcuts import render
from django.views.generic import DetailView
from .models import Master
from django.shortcuts import reverse, redirect
# Create your views here.

def portfolio(request):
    info = Master.objects.all()
    master = Master.objects.get(pk=1)
    employee_id = master.employee_id
    name = master.name
    email = master.email
    password = master.password
    phone_number = master.phone_number
    work_experience = master.work_experience
    position = master.position

    print(employee_id, name, email, password, phone_number, work_experience, position)
    return render(request, 'portfolio/portfolio.html', {'info': info})


def show_master(request, master_id):
    master = Master.objects.get(pk=master_id)
    employee_id = master.employee_id
    name = master.name
    email = master.email
    password = master.password
    phone_number = master.phone_number
    work_experience = master.work_experience
    position = master.position
    master.name = master.name.split()[0]
    print(employee_id, name, email, password, phone_number, work_experience, position)
    return render(request, 'portfolio/master.html', {'master': master})


