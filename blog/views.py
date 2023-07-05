from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
def home(request):
	context = {
		'posts': Post.objects.all()
	}
	#return HttpResponse('<h1>Blog Home</h1>')
	return render(request, 'blog/home.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html' # default to <app>/<model>_<viewtype>.html, which is 'blog/post_list.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']

class PostDetailView(DetailView):
	model = Post
	

def about(request):
#	return HttpResponse('<h1>Blog About</h1>')
	return render(request, 'blog/about.html',{'title':'About'})