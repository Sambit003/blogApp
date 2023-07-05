from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from app.forms import CommentForm
from app.models import Post, Comments

'''
the below function is the view for the home page and it returns the home.html template
'''


def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    comments = Comments.objects.filter(post=post, parent=None)
    form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            parent_obj = None
            if request.POST.get('parent'):
                parent = request.POST.get('parent')
                parent_obj = Comments.objects.get(id=parent)
                if parent_obj:
                    comment_reply = comment_form.save(commit=False)
                    comment_reply.parent = parent_obj
                    comment_reply.post = post
                    comment_reply.save()
                    return HttpResponseRedirect(reverse('post_page', kwargs={'slug': slug}))
            else:
                comment = comment_form.save(commit=False) # commit=False means that the comment is not saved to the database
                post_id = request.POST.get('post_id') # get the post id from the hidden input in the form
                post = Post.objects.get(id = post_id)
                comment.post = post # set the post of the comment to the post we got from the database
                comment.save()
                return HttpResponseRedirect(reverse('post_page', kwargs={'slug': slug}))

    if post.view_count is None:
        post.view_count = 1
    else:
        post.view_count += 1
    post.save()
    context = {'post': post, 'form': form, 'comments': comments}
    return render(request, 'app/post.html', context)


def index(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'app/index.html', context)
