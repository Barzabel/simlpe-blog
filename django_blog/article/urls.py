from django.urls import path
from django_blog.article.views import ArticlesPageView

urlpatterns = [
    path('', ArticlesPageView.as_view(), name='article'),
]