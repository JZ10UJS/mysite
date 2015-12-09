from django.shortcuts import render, get_object_or_404, get_list_or_404
from news.models import *
# Create your views here.


def index(req):
    username = req.session.get('username','')
    article_list = Article.objects.order_by('-pub_date')[:10]
    return render(req, 'news/index.html', {'article_list': article_list, 'username':username})


def details(req, object_id):
    username = req.session.get('username','')
    article = get_object_or_404(Article, pk=object_id)
    article.views_count += 1
    article.save()
    return render(req, 'news/detail.html', {'article': article,'username':username})


def reporter_news(req, object_id):
    username = req.session.get('username','')
    reporter = get_object_or_404(Reporter, pk=object_id)
    return render(req, 'news/reporter_news.html', {'reporter': reporter,'username':username})


def year_archive(req, year):
    article_list = get_list_or_404(Article, pub_date__year=year)
    context = {'article_list':article_list, 'year': year}
    return render(req, 'news/year_archive.html', context)


def month_archive(req, year, month):
    article_list = get_list_or_404(Article, pub_date__year=year, pub_date__month=month)
    context = {'article_list':article_list, 'year': year, 'month': month}
    return render(req, 'news/month_archive.html', context)
