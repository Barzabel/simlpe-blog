from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['name', 'body']


admin.site.register(Article, ArticleAdmin)
