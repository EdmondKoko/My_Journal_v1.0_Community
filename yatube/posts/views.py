from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    """Главная страница. Вывод последних 10 постов отсортированных по дате."""
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    """Страница групп постов."""
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
