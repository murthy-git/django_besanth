from django.shortcuts import render
import datetime


def home(request):
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    if month == 1 and day == 1:
        is_it_new_year = True
    else:
        is_it_new_year = False

    return render(request, "newyear/home.html", {'is_it_new_year': is_it_new_year})
