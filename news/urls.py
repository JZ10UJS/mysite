from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^articles/([0-9]{4})/$', views.year_archive),
    url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
    # url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),
    url(r'^articles/(?P<object_id>[0-9]+)/$', views.details, name='details'),
    url(r'^reporter/(?P<object_id>[0-9]+)/$', views.reporter_news, name='reporter_news'),
]
