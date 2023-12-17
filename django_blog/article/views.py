from django.views.generic.base import TemplateView
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Article

class ArticlesPageView(TemplateView):

    template_name = "articles/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        return context


class ArticleById(View):
    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        article = get_object_or_404(Article, pk=id)
        return render(
            request,
            "articles/article.html",
            context={'article': article}
        )