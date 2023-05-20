from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
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
from .models import Sketch, Session, Employee, User
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return HttpResponse("<h4>about</h4>")


@csrf_exempt
def personal_cabinet_page(request, id=None):

    if request.method == 'POST':

        data = json.loads(request.body.decode('utf-8'))

        selectedTime = data.get('selectedTime')
        selectedMaster = data.get('selectedMaster')
        selectedDate = data.get('selectedDate')
        selectedMonth = data.get('currentMonth')
        selectedYear = data.get('currentYear')
        selectedIdSketch = data.get('sketchId')

        date_string = f"{selectedMonth} {selectedDate} {selectedYear} {selectedTime}"
        date_obj = datetime.strptime(date_string, "%m %d %Y %H:%M")

        user_id = None
        if request.user.is_authenticated:
            user_id = request.user.user_id
            try:
                user = User.objects.get(user_id=user_id)
            except Employee.DoesNotExist:
                return JsonResponse({'result': 'error', 'message': 'Invalid user_id'})

        try:
            sketch = Sketch.objects.get(sketch_id=selectedIdSketch)
        except Sketch.DoesNotExist:
            return JsonResponse({'result': 'error', 'message': 'Invalid sketch ID'})

        try:
            employee = Employee.objects.get(employee_id=selectedMaster)
        except Employee.DoesNotExist:
            return JsonResponse({'result': 'error', 'message': 'Invalid employee ID'})



        session = Session()
        session.date = date_obj
        session.sketch = sketch
        session.employee = employee
        session.user = user

        session.save()



        # Выполните необходимую обработку данных и подготовьте результат
        #print(selectedDate, selectedMaster, selectedTime, selectedIdSketch)
        return JsonResponse({'result': 'success'})

    if id:
        try:
            sketch = Sketch.objects.get(sketch_id=id)
            photo_url = sketch.photo.url
            return render(request, 'main/personal_cabinet.html', {'photo_url': photo_url})
        except Sketch.DoesNotExist:
            pass
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
