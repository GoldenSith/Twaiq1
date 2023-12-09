from django.db import models
from django.contrib.auth.hashers import make_password


# Create your models here.

class Member(models.Model):
    ID = models.AutoField(primary_key=True, unique=True)
    Username = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)
    Password = models.TextField(blank=False)

    def save(self, *args):
        self.Password = make_password(self.Password)
        super().save(*args)


class Post(models.Model):
    ID = models.AutoField(primary_key=True, unique=True)
    Title = models.CharField(max_length=255)
    Content = models.CharField(max_length=255)
    Category = models.CharField(max_length=255)
    Date_published = models.DateField(null=False)


class Comment(models.Model):
    ID = models.AutoField(primary_key=True, unique=True)
    Post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    User_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    Content = models.CharField(max_length=255)
    Date_posted = models.DateField(null=False)


class Category(models.Model):
    ID = models.AutoField(primary_key=True, unique=True)
    Name = models.CharField(max_length=255)
