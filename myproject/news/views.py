from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm


def news_home(request):
    news = Person.objects.all()
    return render(request, 'news/news_home.html', {'news': news})


def create(request):
    error = ''
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/news')
        else:
            error = 'Неправильный e-mail'
    form = PersonForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)
