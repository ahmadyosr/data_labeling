from django.shortcuts import render
from catalogue.models import Snippet 
from django.db.models import Q 
import random
from django.http import HttpResponseRedirect

"""
Catalogue views 
"""
def index(request):
	context = {}
	label =	request.GET.get('label')
	context['categorized_count'] = Snippet.objects.exclude(category=None).count()

	if request.GET.get('remove_last_tender'):
		id_ = request.session['last_tender']
		Snippet.objects.filter(id=id_).update(category='')
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))	

	
	if label:
		id_ = request.GET.get('tender_id')
		Snippet.objects.filter(id=id_).update(category=label)
		request.session['last_tender'] = id_
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

	tenders = Snippet.objects.filter(Q(is_tender=True) | Q(is_auction=True)).filter(category=None)
	context['tender'] = random.choice(tenders)

	return render(request, 'index.html', context)
