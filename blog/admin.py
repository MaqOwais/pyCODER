from django.contrib import admin

# from blog.models import Post

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, BlogComment , BookSection, Topic

@admin.register(Post,BlogComment, BookSection,Topic)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
