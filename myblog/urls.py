from django.conf.urls import patterns, include, url
from django.contrib import admin
from myblog.views import HomeView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'prog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',HomeView.as_view(), name='home'),
    url(r'^blog/', include('blog.urls')),
)