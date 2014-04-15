from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from blog.models import Post, Tag

def index(request):
    latest_post_list = Post.objects.all().order_by('-pub_date')[:5]
    tags_list = Tag.objects.all()
    template = loader.get_template('posts/index.html')
    context = RequestContext(request,{
        'latest_post_list': latest_post_list,
        'tags_list': tags_list,
    })
    return HttpResponse(template.render(context))

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/detail.html', {'post': post})

def article(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    tags = Tag.objects.filter(posts__id__exact=post.id)
    return render(request, 'posts/detail.html', {'post': post, 'tags': tags,})

def results(request, post_id):
    return HttpResponse("You're looking at the results of post %s." % post_id)

def vote(request, post_id):
    return HttpResponse("You're voting on post %s." % post_id)