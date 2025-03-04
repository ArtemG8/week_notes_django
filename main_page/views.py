from django.contrib import messages
from django.http import HttpResponseNotFound
from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from .models import Todo
from .forms import DataForm
from datetime import datetime


# Create your views here.
def main(request):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "friday", "saturday",
                    "sunday"]  # Вывод дней недели на главный экран
    motivational_phrases = [
        "Каждый день — это новый шанс стать лучше.",
        "Ты сильнее, чем думаешь.",
        "Не сдавайся, великие дела требуют времени.",
        "Успех — это сумма маленьких усилий, повторяемых изо дня в день.",
        "Ты можешь больше, чем ты думаешь.",
        "Верь в себя, и всё получится.",
        "Каждый шаг приближает тебя к цели.",
        "Трудности делают нас сильнее.",
        "Не бойся ошибаться, бойся ничего не делать.",
        "Ты — автор своей судьбы.",
        "Мечты сбываются, если идти к ним.",
        "Ты достоин всего, о чем мечтаешь.",
        "Не останавливайся на полпути.",
        "Ты можешь всё, если только захочешь.",
        "Каждый день — это новый старт.",
        "Ты создаешь свое будущее прямо сейчас.",
        "Не бойся начинать заново.",
        "Ты ближе к успеху, чем вчера.",
        "Ты — творец своей жизни.",
        "Не смотри назад, иди вперед.",
        "Ты можешь изменить всё, если захочешь.",
        "Каждый день — это возможность стать лучше.",
        "Ты сильнее, чем кажется.",
        "Не бойся мечтать о большем.",
        "Ты достоин счастья.",
        "Ты можешь всё, если веришь в себя.",
        "Не останавливайся, даже если трудно.",
        "Ты создаешь свою реальность.",
        "Не бойся идти к своей мечте.",
        "Ты можешь всё, если по-настоящему захочешь.",
        "Каждый день — это новый шанс.",
        "Ты сильнее, чем думаешь.",
        "Не сдавайся, даже если трудно.",
        "Ты можешь всё, если веришь в себя.",
        "Каждый шаг — это шаг к успеху.",
        "Ты достоин всего, о чем мечтаешь.",
        "Не бойся начинать заново.",
        "Ты ближе к успеху, чем вчера.",
        "Ты — творец своей жизни.",
        "Не смотри назад, иди вперед.",
        "Ты можешь изменить всё, если захочешь.",
        "Каждый день — это возможность стать лучше.",
        "Ты сильнее, чем кажется.",
        "Не бойся мечтать о большем.",
        "Ты достоин счастья.",
        "Ты можешь всё, если веришь в себя.",
        "Не останавливайся, даже если трудно.",
        "Ты создаешь свою реальность.",
        "Не бойся идти к своей мечте.",
        "Ты можешь всё, если по-настоящему захочешь.",
        "Каждый день — это новый шанс.",
        "Ты сильнее, чем думаешь.",
        "Не сдавайся, даже если трудно.",
        "Ты можешь всё, если веришь в себя.",
        "Каждый шаг — это шаг к успеху.",
        "Ты достоин всего, о чем мечтаешь.",
        "Не бойся начинать заново.",
        "Ты ближе к успеху, чем вчера.",
        "Ты — творец своей жизни.",
        "Не смотри назад, иди вперед.",
        "Ты можешь изменить всё, если захочешь.",
        "Каждый день — это возможность стать лучше.",
        "Ты сильнее, чем кажется.",
        "Не бойся мечтать о большем.",
        "Ты достоин счастья.",
        "Ты можешь всё, если веришь в себя.",
        "Не останавливайся, даже если трудно.",
        "Ты создаешь свою реальность.",
        "Не бойся идти к своей мечте.",
        "Ты можешь всё, если по-настоящему захочешь.",
        "Каждый день — это новый шанс.",
        "Ты сильнее, чем думаешь.",
        "Не сдавайся, даже если трудно.",
        "Ты можешь всё, если веришь в себя.",
        "Каждый шаг — это шаг к успеху.",
        "Ты достоин всего, о чем мечтаешь.",
        "Не бойся начинать заново.",
        "Ты ближе к успеху, чем вчера.",
        "Ты — творец своей жизни.",
        "Не смотри назад, иди вперед.",
        "Ты можешь изменить всё, если захочешь.",
        "Каждый день — это возможность стать лучше.",
        "Ты сильнее, чем кажется.",
        "Не бойся мечтать о большем.",
        "Ты достоин счастья.",
        "Ты можешь всё, если веришь в себя.",
        "Не останавливайся, даже если трудно.",
        "Ты создаешь свою реальность.",
        "Не бойся идти к своей мечте.",
        "Ты можешь всё, если по-настоящему захочешь.",
        "Каждый день — это новый шанс.",
        "Ты сильнее, чем думаешь.",
        "Не сдавайся, даже если трудно.",
        "Ты можешь всё, если веришь в себя.",
        "Каждый шаг — это шаг к успеху.",
        "Ты достоин всего, о чем мечтаешь.",
        "Не бойся начинать заново.",
        "Ты ближе к успеху, чем вчера.",
        "Ты — творец своей жизни.",
        "Не смотри назад, иди вперед.",
        "Ты можешь изменить всё, если захочешь.",
        "Каждый день — это возможность стать лучше.",
        "Ты сильнее, чем кажется.",
        "Не бойся мечтать о большем.",
        "Ты достоин счастья.",
        "Ты можешь всё, если веришь в себя.",
        "Не останавливайся, даже если трудно.",
        "Ты создаешь свою реальность.",
        "Не бойся идти к своей мечте.",
        "Ты можешь всё, если по-настоящему захочешь."
    ]
    model = Todo.objects.all()
    data = {
        'days': days_of_week,
        'motivation': motivational_phrases,
        'todo': model,
    }

    return render(request, 'main_page/main.html', context=data)


def info_ab_days(request, model_name):
    return render(request, 'main_page/info_redirect.html')


def Form(request):
    min_day_value = datetime.today().strftime('%Y-%m-%d')
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            feed = Todo(
                date_of_task=form.cleaned_data['date_of_task'],
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
            )
            feed.save()
            messages.success(request, 'Данные успешно сохранены!')
            return redirect('main_page')
    else:
        form = DataForm()
    data = {
        'form': form,
        'min_day_value': min_day_value,
    }

    return render(request, 'main_page/form.html', data)


def all_data(request):
    if request.method == 'POST':
        todo_id = request.POST.get('todo_id')

        if 'delete' in request.POST:  # крестик удаления записи
            todo = get_object_or_404(Todo, id=todo_id)
            todo.delete()
            return redirect('todo_list')

        is_complete = 'is_complete' in request.POST  # выполнена ли запись
        todo = get_object_or_404(Todo, id=todo_id)
        todo.is_complete = is_complete
        todo.save()

    if 'Old' in request.GET:  # сортировка записей по дате
        todos = Todo.objects.all().order_by('date_of_task')
    else:
        todos = Todo.objects.all().order_by('-date_of_task')

    return render(request, 'main_page/all_data.html', {'todos': todos})


def page_not_found(request, exception):
    return HttpResponseNotFound('Страница не найдена!')
