from django.conf.urls import url
from login import views
# Create your views here.
urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^regist/', views.regist, name='regist'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^search/', views.search, name='search'),
]