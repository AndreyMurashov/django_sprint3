from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Post
import datetime


def index(request):
    today = datetime.datetime.now()
    template_name = 'blog/index.html'
    context = {
        'post_list': Post.objects.filter(pub_date__lte=today,
                                         is_published=True,
                                         category__is_published=True)
                         .order_by('-pk')[0:5]}
    return render(request, template_name, context)


def post_detail(request, pk):
    today = datetime.datetime.now()
    template_name = 'blog/detail.html'
    try:
        post = get_object_or_404(Post.objects.filter(pub_date__lte=today,
                                                     is_published=True,
                                                     category__is_published=True), pk=pk)
        context = {'post': post}
        return render(request, template_name, context)
    except IndexError:
        return HttpResponseNotFound('<h1>404 Page not found</h1>')


def category_posts(request, category_slug):
    today = datetime.datetime.now()
    template_name = 'blog/category.html'
    cat_posts = get_list_or_404(
        Post.objects.select_related('category')
        .filter(category__slug=category_slug,
                is_published=True,
                pub_date__lte=today).order_by('-pk'),
        category__is_published=True
    )

    context = {'post_list': cat_posts,
               'category': category_slug
               }
    return render(request, template_name, context)
