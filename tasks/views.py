from django.shortcuts import render

tasks = ['read', 'movie', 'write', 'python']


def home(request):
    return render(request, "tasks/home.html", {
        'items': tasks
    })


def add(request):
    return render(request, "tasks/add.html")
