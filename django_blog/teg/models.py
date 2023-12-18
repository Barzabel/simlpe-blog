from django.db import models


class Tegs(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
