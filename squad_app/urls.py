""" URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView
from squad_health_check_api.views import squad_loginView

app_name="squad"
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'), #/admin page
    path('login/', squad_loginView.as_view(), name='login'), #login for squad members page
    path('profile/', TemplateView.as_view(template_name='squad/profile.html'), name='profile'), #profile page for squad member upon login
]
