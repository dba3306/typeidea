from django.shortcuts import render
from .models import Post, Tag, Category
from django.http import HttpResponse
# Create your views here.


def post_list(request, category_id=None, tag_id=None):
    tag = None
    category = None

    if tag_id:
        post_list, tag = Post.get_by_tag(tag_id)
    elif category_id:
        post_list, tag = Post.get_by_category(category_id)
    else:
        post_list = Post.latest_posts()
    context = {
        'category': category,
        'tag': tag,
        'post_list': post_list
    }
    return render(request, 'blog/list.html', context={'context': context})


def post_detail(request, post_id=None):
    # return HttpResponse('detail')
    # return render(request, 'blog/detail.html', context={'name': 'post_detail'})
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None
    return render(request, 'blog/detail.html', context={'post': post})