# Create your views here.
from blog.models import Blog
from django.shortcuts import render, get_object_or_404


def list(request):
	blog_list = Blog.objects.order_by('-pub_date')[:3]
	context = {'blog_list':blog_list}
	return render(request,'blog.html',context)

def detail(request, blog_id):
	blog = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'blog_detail.html', {'blog': blog})