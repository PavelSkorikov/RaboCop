"""RaboCop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    # подключаем базовую аутентификацию Django Rest (сессии)
    path ('api/v1/base-auth/', include('rest_framework.urls')),
    # подключаем аутентификацию с помощью бибилиотеки Djoser (сессии)
    path ('api/v1/auth/', include('djoser.urls')),
    # подключаем аутентификацию помощью бибилиотеки Djoser (токены)
    # токены будут выдаваться пользователю по адресу http://localhost:8000/api/v1/auth_token/token/login
    path ('api/v1/auth_token/', include('djoser.urls.authtoken')),
    # путь к приложению FindJob
    path('api/v1/findjob/', include('FindJob.urls')),
]
