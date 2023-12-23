from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Article
from django_blog.teg.models import Tegs


class ArticlesPageView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('query', '')
        select_tegs = request.GET.getlist('tegs', None)
        tegs = Tegs.objects.all()
        if select_tegs:
            articles = Article.objects.filter(Q(name__icontains=query), tegs__in=select_tegs).distinct()
        else:
            articles = Article.objects.filter(Q(name__icontains=query))
        return render(
            request,
            "articles/index.html",
            context={
                'articles': articles,
                'query': query,
                'tegs': tegs,
            }
        )


class ArticleById(View):
    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        article = get_object_or_404(Article, pk=id)
        return render(
            request,
            "articles/article.html",
            context={'article': article}
        )
