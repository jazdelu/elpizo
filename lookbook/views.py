# Create your views here.
from lookbook.models import Lookbook
import string
from django.shortcuts import render, get_object_or_404


def list(request):
	lookbook_list = Lookbook.objects.order_by('pub_date')
	context = {'lookbook_list':lookbook_list}
	return render(request,'lookbook.html',context)

def detail(request, lookbook_id):
	lookbook = get_object_or_404(Lookbook, pk=lookbook_id)
	next = 0
	prev = 0
	lookbook_id = string.atoi(lookbook_id) 
	if Lookbook.objects.filter(pk=(lookbook_id+1)):
		next = lookbook_id+1

	if Lookbook.objects.filter(pk=(lookbook_id-1)):
		prev = lookbook_id-1

	return render(request, 'lookbook_content.html', {'lookbook': lookbook,'next':next, 'prev':prev})