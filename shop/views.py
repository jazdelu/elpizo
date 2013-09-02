# Create your views here.
from django.shortcuts import render

def shop(request):
	return render(request,'shop.html',)