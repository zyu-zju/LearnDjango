from django.shortcuts import render
#from django.http import HttpResponse
from .models import Post

posts = [
	{
		'author': 'CoreyMS',
		'title': 'Blog Post 1',
		'content':'First post content',
		'date_posted': 'Jul 3, 2023'
	},
	{
		'author': 'Billy YU',
		'title': 'Blog Post 2',
		'content':'second post content',
		'date_posted': 'Jul 4, 2023'
	}
]

# Create your views here.
def home(request):
	context = {
		'posts': Post.objects.all()
	}
	#return HttpResponse('<h1>Blog Home</h1>')
	return render(request, 'blog/home.html', context)


def about(request):
#	return HttpResponse('<h1>Blog About</h1>')
	return render(request, 'blog/about.html',{'title':'About'})