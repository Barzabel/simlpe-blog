from django.urls import path
from django_blog.article.views import (
    ArticlesPageView,
    ArticleById,
    ArticleByTeg
)

urlpatterns = [
    path('', ArticlesPageView.as_view(), name='article'),
    path('teg/<str:teg>/', ArticleByTeg.as_view(), name='article_by_teg'),
    path('<int:id>/', ArticleById.as_view(), name='article_by_id'),
]