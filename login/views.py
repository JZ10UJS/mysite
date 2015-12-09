# coding=utf-8
from django.shortcuts import render
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from login.models import *
from django.core.urlresolvers import reverse
from news.models import *
# Create your views here.

class userForm(forms.Form):
    username = forms.CharField(label=u'用户名：', max_length=64)
    password = forms.CharField(label=u'密码：', widget=forms.PasswordInput())


class registForm(forms.Form):
    username = forms.CharField(max_length=64)
    password1 = forms.CharField(max_length=64)
    password2 = forms.CharField(max_length=64)


def login(req):
    if req.method == 'POST':
        userform = userForm(req.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            req.session['username'] = username
            req.session['password'] = password
            user = User.objects.filter(username__exact=username, password__exact=password)
            if user:
                return render(req, 'login/info.html', {'username': username})
            else:
                return HttpResponseRedirect(reverse('login:login'))
    else:
        username = req.session.get('username', '')

    return render(req, 'login/index.html', {'username': username})


def logout(req):
    del req.session['username']
    return HttpResponseRedirect('/')


def search(req):
    if 'q' in req.GET and req.GET['q']:
        q = req.GET['q']
        article_list = Article.objects.filter(headline__icontains=q).order_by('-pub_date')
        if len(article_list) == 0:
            message = '%s not found in news' % q
            return render(req, 'login/search_result.html',{'message':message})
        return render(req, 'news/index.html',{'article_list':article_list})
    else:
        message = 'No search query given'
    return render(req, 'login/search_result.html', {'message':message})


def regist(req):
    if req.method == 'POST':
        registform = registForm(req.POST)
        if registform.is_valid():
            username = registform.cleaned_data['username']
            password1 = registform.cleaned_data['password1']
            password2 = registform.cleaned_data['password2']
            if password1 == password2:
                try:
                    user = User(username=username, password=password1)
                    user.save()
                    return HttpResponse('注册成功，%s' % user)
                except:
                    return HttpResponse('用户名已经注册')
            else:
                return HttpResponse('两次密码输入不同')
    else:
        return render(req, 'login/regist.html')
