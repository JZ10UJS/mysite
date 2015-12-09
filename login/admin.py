from django.contrib import admin
from login.models import *
# Register your models here.
class userAdmin(admin.ModelAdmin):
	list_display = ('username', 'password')

admin.site.register(User, userAdmin)