from django.shortcuts import render
from django.http import HttpResponse
import random
from db3.apps.blog.models import Post
from db3.apps.blog.models import Key_word
from db3.apps.blog.models import Author


def hello():
    form = '<button>Test me for me pls!?!</button>'
    return form


def btn():
    i = 1
    f = 1
    b = ''
    for i in range(1, 10):
        b += '{}'.format(str(i) + '*' + str(f) + '=' + str(i * f))
        i += 1
    return b


def author_posts():

    # for post1 in posts:
    #     for author1 in authors:
    #         if post1.author.id == author1.id:
    #             a.append(post1.post_title)
    return a


def index(request):
    post_list = Post.objects.all()
    key_word = Post.objects.all()
    authors = Author.objects.all()
    context = {
        'posts': post_list,
        'key_word': key_word,
        'authors': authors,
    }
    return render(request, "index.html", context)


def about(request):
    context = {


    }
    return render(request, "about.html", context)


def contacts(request):
    context = {


    }
    return render(request, "contacts.html", context)


def post(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'title': Post.post_title,
        'text': Post.post_text,
        'post': post,
    }
    return render(request, "posts.html", context)


def author(requset, author_id):
    author = Author.objects.get(id=author_id)
    a = []
    posts = Post.objects.get(author=author)
    a.append(posts.post_title)
    context = {
        'author': author,
        'posts': a,
    }
    return render(requset, "author.html", context)
