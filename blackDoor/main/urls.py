"""
URL configuration for blackDoor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('personal_cabinet/', views.personal_cabinet_page, name='personal_cabinet'),
    path('personal_cabinet/<int:id>/', views.personal_cabinet_page, name='personal_cabinet'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('sketch/', views.sketch, name='sketch'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('add/', views.add_sketches, name='add_sketches'),
    path('feedback/', views.feedback, name='feedback'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

