from django.shortcuts import render
from .models import Blog_Post
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    posts = Blog_Post.objects.all()
    return render(request, 'index.html',{'posts': posts})

def detail(request, slug):
    post = Blog_Post.objects.get(slug=slug)
    comments = post.comments.order_by('-id')
    new_comment = None
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(reverse('blog_detail',args=[str(post.slug)]))
    else:
        form = CommentForm()
        
    context = {'post': post, 'form': form, 'comments': comments}
    return render(request, 'blog_detail.html',context)