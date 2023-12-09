from django.contrib import admin
from .models import *


class MemberAdmin(admin.ModelAdmin):
    list_display = ("Username", "Email")


class PostAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Content', 'Category', 'Date_published')


class CommentAdmin(admin.ModelAdmin):
    def get_post_id(self, obj):
        return obj.Post_id.ID

    def get_user_id(self, obj):
        return obj.User_id.ID

    list_display = ('get_post_id', 'get_user_id', 'Content', 'Date_posted')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Name',)


# Register your models here.

admin.site.register(Member, MemberAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
