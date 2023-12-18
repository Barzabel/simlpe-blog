from django.db import models
from django_blog.teg.models import Tegs



class Article(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tegs = models.ManyToManyField(Tegs, blank=True, related_name="Article_list")

    def __str__(self):
        return self.name
