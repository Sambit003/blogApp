from django.shortcuts import render
from app.models import Post
'''
the below function is the view for the home page and it returns the home.html template
'''
def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    context = {'post': post}
    return render(request, 'app/post.html', context)

def index(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'app/index.html', )