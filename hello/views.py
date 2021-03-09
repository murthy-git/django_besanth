from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "hello/home.html")


def say_hello(request, name):
    return render(request, "hello/say.html", {'full_name': name})


