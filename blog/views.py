from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from blog.models import Post, Tag, Like

def index(request):
    latest_post_list = Post.objects.all().order_by('-pub_date')[:5]
    tags_list = Tag.objects.all().order_by('name')
    template = loader.get_template('posts/index.html')
    context = RequestContext(request,{
        'latest_post_list': latest_post_list,
        'tags_list': tags_list,
    })
    return HttpResponse(template.render(context))

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    num_likes = post.like_set.all().count()
    return render(request, 'posts/detail.html', {'post': post, 'likes':num_likes})

def article(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    tags = Tag.objects.filter(posts__id__exact=post.id)
    return render(request, 'posts/detail.html', {'post': post, 'tags': tags})

def results(request, post_id):
    return HttpResponse("You're looking at the results of post %s." % post_id)

def like(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    return render(request, 'posts/detail.html', {'post': post}) 

# def like(request, post_slug):
#     post = get_object_or_404(Post, slug=post_slug)
#     new_like, created = Like.objects.get_or_create(user=get_client_ip(request))
#     if created:
#         return render(request, 'posts/detail.html', {'post': post})
#     else:
#         return render(request, 'posts/detail.html', {'post': post})
#     
# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip