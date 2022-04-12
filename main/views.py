import datetime
from django.shortcuts import render, redirect
from .forms import CreateAbcForm
from .models import Abc
from django.http import HttpResponse


# from django.urls import reverse

# def ind ex(request):
#     return HttpResponse("main.views")

def index(request):
    return render(request, 'main/index.html')


# def index(request):
#     name_main="index"
#     redirect_url=reverse ('index', args=(name_main))
#     return render(request, redirect_url)

def list_main(request):
    list_main = (1, 2, 3, 4, 5)
    print(list_main)
    dict_main = {'x': 1, 'y': 2}
    print(dict_main)
    context = {'list_main': list_main, 'dict_main': dict_main}  # будем передавать в шаблон как один общий объект
    return render(request, 'main/list_main.html', context)


def form_create(request):
    # print('request.method: ', request.method )
    if request.method == 'POST':
        form = CreateAbcForm(request.POST)
        if form.is_valid():
            form.save()
            print("form: ", form)
            return redirect('main:result')
    else:
        print("else: ")
        form = CreateAbcForm()
    print('form:',form)
    context = {
        'form': form
    }
    print(context)
    return render(request, 'main/form_create.html', context)


def result(request):
    # rows = Abc.objects.values_list()
    rows = Abc.objects.values_list()

    for row in rows:
        list_main = [row[2],row[3],row[4]]
        if (list_main[0] + list_main[1] == list_main[2]):
            result = "равна"
        else:
            result = "не равна"
        list_main.append(result)
        print('list_main: ', list_main)
        task_main=list()
        task_main.append(row[1])

    context = {'task_main': task_main, 'list_main': list_main}
    return render(request, 'main/result.html', context)


def datetime_nov(request):
    now = list()
    now.append(datetime.datetime.now())
    print('datetime.datetime.now(): ', now)
    list_main = now
    print(list_main)
    context = {'list_main': list_main}
    return render(request, 'main/datetime_now.html', context)
