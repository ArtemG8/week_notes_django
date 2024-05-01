from django.shortcuts import render, HttpResponse, HttpResponseRedirect


# Create your views here.
def main(request):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    data = {
        'days': days_of_week
    }
    return render(request, 'main_page/main.html', context=data )
