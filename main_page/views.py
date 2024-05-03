from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Days

# Create your views here.
def main(request):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    data = {
        'days': days_of_week
    }
    return render(request, 'main_page/main.html', context=data)


def info_ab_days(request):
    data = {
        'days': Days.objects.all()

    }
    return render(request, 'main_page/info_redirect.html', context=data)
