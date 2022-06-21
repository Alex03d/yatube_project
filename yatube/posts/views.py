# check
from django.http import HttpResponse


def index(request):
    return HttpResponse('Самая главная страница')


def group_posts(request, slug):
    return HttpResponse('Типо посты группы')