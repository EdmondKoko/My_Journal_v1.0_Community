from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    """Главная страница. Передаёт в шаблон posts/index.html десять последних объектов модели Post."""
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    """Страница списка постов. Передаёт в шаблон posts/group_list.html десять последних объектов модели Post,
    отфильтрованных по полю group."""
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
