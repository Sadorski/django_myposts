from django.shortcuts import render, HttpResponse, redirect
from models import Post
  # the index function is called when root is visited
def index(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'myposts/index.html', context)

def process(request):
    if request.method == 'POST':
        Post.objects.create(desc=request.POST['desc'])

    context = {
		'posts': Post.objects.all()
    }
    return render(request, 'myposts/posts.html', context)

