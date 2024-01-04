from django.urls import path
from django_blog.article.views import (
    ArticlesPageView,
    ArticleById,
    ArticleFormCreateView,
    ArticleFormEditView,
)

urlpatterns = [
    path('', ArticlesPageView.as_view(), name='article'),
    path('<int:id>/edit', ArticleFormEditView.as_view(), name='article_edit'),
    path('<int:id>/', ArticleById.as_view(), name='article_by_id'),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
]