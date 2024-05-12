from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Monday, Tuesday, Wednesday
from .forms import DataForm
from datetime import datetime


# Create your views here.
def main(request):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "friday", "saturday",
                    "sunday"]  # Вывод дней недели на главный экран
    data = {
        'days': days_of_week
    }
    return render(request, 'main_page/main.html', context=data)


def info_ab_days(request, model_name):
    if model_name == 'Monday':
        model = Monday.objects.values_list('task', 'date_of_create')
    elif model_name == 'Tuesday':
        model = Tuesday.objects.values_list('task', flat=True)
    elif model_name == 'model3':
        model = Wednesday.objects.values_list('task', flat=True)
    else:
        # Обработка случаев, когда модель не найдена
        model = None

    return render(request, 'main_page/info_redirect.html', {'days': model})


def Form(request):
    min_day_value = datetime.today().strftime('%Y-%m-%d')
    print(min_day_value)
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            feed = Monday(
                date_of_create=form.cleaned_data['date_of_create'],
                task=form.cleaned_data['task']
            )
            feed.save()
            return HttpResponseRedirect('/')
    else:
        form = DataForm()
    data = {
        'form': form,
        'min_day_value': min_day_value,
    }

    return render(request, 'main_page/form.html', data)
#
#
# def done(request):
#     data = {
#         'user_name': Feedback.name
#     }
#     return render(request, 'feedback/donne.html', context=data)
