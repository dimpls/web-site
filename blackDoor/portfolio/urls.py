from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('master<str:master_id>/', views.show_master, name='show_master'),

]