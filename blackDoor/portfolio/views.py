from django.shortcuts import render
from django.views.generic import DetailView
from main.models import User
import json

from django.shortcuts import reverse, redirect
# Create your views here.


def show_master(request, master_id):
    master_obj = User.objects.filter(username=master_id)
    return render(request, 'portfolio/master.html', {'master': master_obj[0]})

