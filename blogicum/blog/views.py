from django.http import HttpResponseNotFound
from django.shortcuts import render
from post.models import Post

def index(request):
    template_name = 'blog/index.html'
    posts = Post.objects.all()
    newlist = sorted(posts, key=lambda d: -d['id'])
    context = {'posts': newlist}
    return render(request, template_name, context)


def post_detail(request, id):
    template_name = 'blog/detail.html'
    try:
        context = {'post': posts[id]}
        return render(request, template_name, context)
    except IndexError:
        return HttpResponseNotFound('<h1>404 Page not found</h1>')


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    context = {'category_slug': category_slug}
    return render(request, template_name, context)
