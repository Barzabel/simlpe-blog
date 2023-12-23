from django.urls import path
from django_blog.article.views import (
    ArticlesPageView,
    ArticleById,
)

urlpatterns = [
    path('', ArticlesPageView.as_view(), name='article'),
    path('<int:id>/', ArticleById.as_view(), name='article_by_id'),
]