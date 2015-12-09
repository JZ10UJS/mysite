from django.contrib import admin
from news.models import *
# Register your models here.

class articleAdmin(admin.ModelAdmin):
    list_display = ('headline', 'pub_date', 'reporter')



admin.site.register(Article, articleAdmin)
admin.site.register(Reporter)