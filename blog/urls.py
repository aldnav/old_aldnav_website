'''
Created on Apr 13, 2014

@author: Aldrin
'''
from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
     # ex: /blog/
    url(r'^$', views.index, name='index'),
    # ex: /blog/5/
    url(r'^(?P<post_id>\d+)/$', views.detail, name='detail'),
    # ex: /blog/title-of-article/
    url(r'^(?P<post_slug>[-\w]+)/$', views.article, name='article'),
    # ex: /blog/5/results/
    url(r'^(?P<post_id>\d+)/results/$', views.results, name='results'),
    # ex: /blog/5/vote/
    url(r'^(?P<post_id>\d+)/vote/$', views.vote, name='vote'),
)