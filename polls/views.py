from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from polls.models import *
from django.core.urlresolvers import reverse
from django.utils import timezone

from django.views import generic
# Create your views here.

def index(req):
	latest_question_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
	return render(req, 'polls/index.html', {'latest_question_list':latest_question_list})
	
def detail(req, question_id):
	question = get_object_or_404(Question, pk=question_id)
	if question.pub_date <= timezone.now():
		return render(req, 'polls/detail.html', {'question':question})
	else:
		raise Http404('Page not found')
		
def results(req, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(req, 'polls/results.html', {'question':question})

"""
class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'
	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'
"""
def vote(req, question_id):
	p = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=req.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(req, 'polls/detail.html',{
			'question': p,
			'error_message': 'You did not select a choice',
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
