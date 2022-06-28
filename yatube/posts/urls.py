# posts/urls.py
# check
from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    path('group_list/', views.group_list, name='group_list'),
    # path('group/<slug:slug>/', views.group_list),
    path('', views.index, name='index'),
]