from django.http import HttpResponse
from django.template import loader
from .models import *


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def members(request):
    myusers = Member.objects.all().values()
    template = loader.get_template('users.html')
    context = {
        'myusers': myusers,
    }
    return HttpResponse(template.render(context, request))


def blogs(request):
    myblogs = Post.objects.all().values()
    template = loader.get_template('blogs.html')
    context = {
        'myblogs': myblogs,
    }
    return HttpResponse(template.render(context, request))


def blog_details(request, id):
    mydetail = Post.objects.get(ID=id)
    template = loader.get_template('blogdetails.html')
    context = {
        'mydetail': mydetail,
    }
    return HttpResponse(template.render(context, request))


def categories(request):
    mycategory = Category.objects.all().values()
    template = loader.get_template('categories.html')
    context = {
        'mycategory': mycategory,
    }
    return HttpResponse(template.render(context, request))


def comments(request):
    mycomment = Comment.objects.all()
    template = loader.get_template('comments.html')
    context = {
        'mycomment': mycomment,
    }
    return HttpResponse(template.render(context, request))