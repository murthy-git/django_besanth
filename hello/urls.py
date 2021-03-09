from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('<str:name>/', views.say_hello, name='say-hello'),
]