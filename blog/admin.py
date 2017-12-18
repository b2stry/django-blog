from django.contrib import admin
from . import models


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
