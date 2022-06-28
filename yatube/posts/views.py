# check
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # Адрес шаблона сохраним в переменную, это не обязательно, но удобно
    template = 'posts/index.html'
    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
    title = 'Yatube'
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Это главная страница проекта Yatube',
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)


def group_list(request):
    template = 'posts/group_list.html'
    title = 'Yatube'
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Здесь будет информация о группах проекта Yatube',
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)


# def group_posts(request, slug):
#     return HttpResponse('Типо посты группы')