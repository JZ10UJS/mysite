from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(req):
    username = req.session.get('username','')
    values = req.META.items()
    values.sort()
    return render(req, 'home/index.html',{'username':username,'values':values})
