from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Days
from .forms import DataForm


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


# def form(request):
#     return render(request, 'main_page/form.html')
def Form(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            feed = Days(
                monday=form.cleaned_data['monday'],
                tuesday=form.cleaned_data['tuesday'],
                # feedback=form.cleaned_data['feedback'],
            )
            feed.save()
            return HttpResponseRedirect('/')
    else:
        form = DataForm()

    return render(request, 'main_page/form.html', context={'form': form})
#
#
# def done(request):
#     data = {
#         'user_name': Feedback.name
#     }
#     return render(request, 'feedback/donne.html', context=data)
