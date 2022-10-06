# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Post, Group

#Главная страница
def index(request):
    template = 'posts/index.html'
    title= "Последние обновления на сайте"
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, template, context)

#Списки групп
def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = "Записи сообщества"
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'title': title,
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)