from django.urls import path

from . import views

app_name = 'posts'

"""Создаем urls для главной страницы и страницы Group"""
urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug>/', views.group_posts, name='group_list'),
]
