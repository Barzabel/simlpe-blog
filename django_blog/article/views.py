from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Article
from .forms import ArticleForm
from django_blog.teg.models import Tegs
from django.db.models import Count





class ArticlesPageView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('query', '')
        select_tegs = request.GET.getlist('tegs', None)
        tegs = Tegs.objects.all()
        if select_tegs:
            articles = Article.objects.filter(
                Q(name__icontains=query),
                tegs__in=select_tegs
            ).annotate(num_tegs=Count('tegs')).filter(num_tegs=len(select_tegs))
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


class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(
            request,
            "articles/form.html",
            context={
                'form': form,
            }
        )

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article')
        return render(
            request,
            "articles/form.html",
            context={
                'form': form,
            }
        )


class ArticleFormEditView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        article = get_object_or_404(Article, pk=id)
        form = ArticleForm(instance=article)
        return render(
            request,
            "articles/form_edit.html",
            context={
                'form': form,
                'article_id': id,
            }
        )

    def post(self, request, *args, **kwargs):
        id = kwargs['id']
        article = get_object_or_404(Article, pk=id)
        form = ArticleForm(request.POST,  instance=article)
        if form.is_valid():
            form.save()
            return redirect('article')
        return render(
            request,
            "articles/form_edit.html",
            context={
                'form': form,
                'article_id': id,
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
