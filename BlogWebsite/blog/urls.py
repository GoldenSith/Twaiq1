from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.members, name='users'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/blogdetails/<int:id>', views.blog_details, name='blogdetails'),
    path('comments/blogdetails/<int:id>', views.blog_details, name='blogdetails'),
    path('categories/', views.categories, name='categories'),
    path('comments/', views.comments, name='comments'),
]
