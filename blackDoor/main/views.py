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
from .models import Sketch, Session, User, Review
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
from django.db.models import Exists, OuterRef
from django.contrib.auth import get_user_model
from django.db.models import Q

def index(request):
    return render(request, 'main/index.html')


def about(request):
    return HttpResponse("<h4>about</h4>")


def cancelled(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            ses_id = data.get('session_id')
            session = Session.objects.get(session_id=ses_id)
            session.status = 'cancelled'
            session.save()
        except Session.DoesNotExist:
            print('[ERROR] Cancel function error')

        user_id = request.user.user_id
        sessions = Session.objects.filter(user_id=user_id)  # Таблица
        reviewed_sessions = Session.objects.filter(  # объект сессий
            Exists(Review.objects.filter(session_id=OuterRef('session_id')))
        )
        reviews = Review.objects.filter(session__in=reviewed_sessions)

        ratings = {}
        for ses, mark in zip(reviewed_sessions, reviews):  # оценки в каждой сессии ревью
            session_id = ses.session_id
            rate = mark.rate
            ratings[session_id] = rate

        return render(request, 'main/personal_cabinet.html', {'sessions': sessions, 'review': reviewed_sessions,
                                                              'marks': ratings})


def feedback(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        rate = data.get('rate')
        experience = data.get('experience')
        selectedEmployee = data.get('selectedEmployeeName') #id работника
        ses_id = data.get('session_id')

        user_id = None
        if request.user.is_authenticated:
            user_id = request.user.user_id
            user = User.objects.get(user_id=user_id)

        employee = User.objects.get(user_id=selectedEmployee)


        session = Session.objects.get(session_id=ses_id)


        review = Review()
        review.user = user
        review.employee_id = selectedEmployee
        review.body = experience
        review.rate = rate
        review.session = session
        review.save()

        data = {
            'rate': rate,
            'experience': experience,
            'employee_id': selectedEmployee
        }


    user_id = request.user.user_id
    sessions = Session.objects.filter(user_id=user_id)  # Таблица
    reviewed_sessions = Session.objects.filter(             #объект сессий
        Exists(Review.objects.filter(session_id=OuterRef('session_id')))
    )
    reviews = Review.objects.filter(session__in=reviewed_sessions)

    ratings = {}
    for ses, mark in zip(reviewed_sessions, reviews):  # оценки в каждой сессии ревью
        session_id = ses.session_id
        rate = mark.rate
        ratings[session_id] = rate

    return render(request, 'main/personal_cabinet.html', {'sessions': sessions, 'review': reviewed_sessions,
                                                          'marks': ratings})

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

            user = User.objects.get(user_id=user_id)

        try:
            sketch = Sketch.objects.get(sketch_id=selectedIdSketch)
        except Sketch.DoesNotExist:
            return JsonResponse({'result': 'error', 'message': 'Invalid sketch ID'})


        employee = User.objects.get(user_id=selectedMaster)


        session = Session()
        session.date = date_obj
        session.sketch = sketch
        session.employee_id = employee.user_id
        session.user = user

        session.save()

        return JsonResponse({'result': 'success'})

    if id:
        try:
            sketch = Sketch.objects.get(sketch_id=id)
            photo_url = sketch.photo.url
            user_id = request.user.user_id
            sessions = Session.objects.filter(user_id=user_id)
            reviewed_sessions = Session.objects.filter(  # объект сессий
                Exists(Review.objects.filter(session_id=OuterRef('session_id')))
            )
            reviews = Review.objects.filter(session__in=reviewed_sessions)
            ratings = {}
            for ses, mark in zip(reviewed_sessions, reviews):  # оценки в каждой сессии ревью
                session_id = ses.session_id
                rate = mark.rate
                ratings[session_id] = rate
            return render(request, 'main/personal_cabinet.html', {'photo_url': photo_url,
                                                                  'sessions': sessions, 'review': reviewed_sessions, 'marks': ratings})
        except Sketch.DoesNotExist:
            pass

    user_id = request.user.user_id
    sessions = Session.objects.filter(user_id=user_id)
    #for i in sessions:
        #print(i.employee_id, "!!!!") #id работника
    reviewed_sessions = Session.objects.filter(  # сессии которые уже оценены
        Exists(Review.objects.filter(session_id=OuterRef('session_id')))
    )
    reviews = Review.objects.filter(session__in=reviewed_sessions)
    ratings = {}
    for ses, mark in zip(reviewed_sessions, reviews): # оценки в каждой сессии ревью
        session_id = ses.session_id
        rate = mark.rate
        ratings[session_id] = rate
    return render(request, 'main/personal_cabinet.html',
                  {'sessions': sessions, 'review': reviewed_sessions, 'marks': ratings})


def post_review(request):
    if request.method == 'POST':
        rate = request.POST.get('rate')  # Получение значения выбранного рейтинга
        description = request.POST.get('description')  # Получение значения текстового поля

        # Дальнейшая обработка полученных значений, например, сохранение в базе данных
        # ...

        return redirect('success')  # Перенаправление на страницу успешной отправки

    return render(request, 'review_form.html')


def staff(request):

    user_id = request.user.user_id
    sessions = Session.objects.filter(employee_id=user_id)  # Таблица
    for i in sessions:
        print(i.status, 'staff')

    reviews = Review.objects.filter(session_id__in=Session.objects.values_list('session_id', flat=True))
    print(reviews)
    for i in reviews:
        print("ses=", i.session_id, "rate", i.rate)
    session_rate_dict = {}
    for review in reviews:
        session_rate_dict[review.session_id] = review.rate

    print(session_rate_dict)
    #for ses, mark in zip(reviewed_sessions, reviews):  # оценки в каждой сессии ревью
    #    session_id = ses.session_id
    #    rate = mark.rate
    #    ratings[session_id] = rate

    #print(ratings)

    return render(request, 'main/staff.html', {'sessions': sessions, 'marks': session_rate_dict})


def accept_cancel(request):
    if request.method == 'POST':
        button_value = request.POST.get('button_value')
        values = button_value.split('|')
        print(values)
        session = Session.objects.get(session_id=values[1])
        if values[0] == 'completed':
            session.status = 'completed'
        else:
            session.status = 'cancelled'

        try:
            session.save()
        except Exception as e:
            print('[ERROR]: accept_cancel', str(e))



    user_id = request.user.user_id
    sessions = Session.objects.filter(employee_id=user_id)  # Таблица
    for i in sessions:
        print(i.status, 'acc')

    reviews = Review.objects.filter(session_id__in=Session.objects.values_list('session_id', flat=True))
    print(reviews)
    for i in reviews:
        print("ses=", i.session_id, "rate", i.rate)
    session_rate_dict = {}
    for review in reviews:
        session_rate_dict[review.session_id] = review.rate

    return render(request, 'main/staff.html', {'sessions': sessions, 'marks': session_rate_dict})

def portfolio(request):
    employees = User.objects.filter(is_staff=True)
    return render(request, 'portfolio/portfolio.html', {'employees': employees})


def sketch(request):
    sketches = Sketch.objects.all()
    return render(request, 'main/sketch.html', {'sketches': sketches})


def add_sketches(request):
    # Предположим, у вас есть список путей к фотографиям, которые вы хотите добавить
    photo_paths = 'main/static/main/img/master6.png'

    tmp = 1000.0
    k = 6

    User = get_user_model()

    master = User()
    master.first_name = 'Евгений'
    master.last_name = 'Морозов'
    master.email = 'Evg123456@gmail.com'
    master.username = 'Evg123456'
    master.is_staff = True
    master.set_password('Evg123456')
    # Заполняем остальные поля пользователя, если необходимо
    master.date_of_birth = '2002-11-20'
    master.phone_number = '79113345563'
    master.tattoos_made = 0
    # Сохраняем фотографию мастера
    master.photo.save('master' + str(k) + '.png', open(photo_paths, 'rb'))
    # Заполняем поле 'price' текущим значением tmp
    # Сохраняем объект User в базе данных
    master.save()



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
