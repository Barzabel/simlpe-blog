from django.contrib import admin
from .models import Tegs


class TegAdmin(admin.ModelAdmin):
    search_fields = ['name',]


admin.site.register(Tegs, TegAdmin)

