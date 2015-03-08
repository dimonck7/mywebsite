#coding: utf-8
from django.conf.urls import patterns, url

from blog.views import PostsListView, PostDetailView, CreatView, ComingView,  VerListView

urlpatterns = patterns('',
url(r'^$', PostsListView.as_view(), name='list'),
url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()),
url(r'^creat/', CreatView.as_view(),name='creat'),
url(r'^coming/', ComingView.as_view(),name='coming'),
url(r'^ver/', VerListView.as_view(),name='ver'),

)
