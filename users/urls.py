"""Определяет схемы URL для пользователей"""

from django.urls import path, include

from . import views

app_name='users'
urlpatterns = [
    # Выход из аккаунта пользователя.
    path('logout', views.logout_view, name='logout'),
    # Включить URL авторизации по умолчанию.
    path('', include('django.contrib.auth.urls')),
    # Страница регистрации.
    path('register/', views.register, name='register'),
]