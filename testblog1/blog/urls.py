from django.conf.urls.defaults import *
from django.conf import settings

from django.views.generic import list_detail

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from blogs.models import Blog

blog_info = {
        "queryset": Blog.objects.filter(active=True),
        }

urlpatterns = patterns('',
    # Example:
    # (r'^blog/', include('blog.foo.urls')),
    #url(r'^$', 'blogs.views.blog_index', name='home'),
    url(r'^$', list_detail.object_list, blog_info, name='home'),
    url(r'^blog/(?P<slug>[-\w]+)/$', 'blogs.views.blog', name='blog'),
    url(r'^blog/(?P<slug>[-\w]+)/(?P<y>\d{4})/$', 'blogs.views.year', name='year'),
    url(r'^blog/(?P<slug>[-\w]+)/(?P<y>\d{4})/(?P<m>\d{2})/$', 'blogs.views.month', name='month'),

    url(r'^blog/(?P<blog>[-\w]+)/post/(?P<slug>[-\w]+)/$', 'blogs.views.post', name='post'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

)

if settings.DEBUG:
    urlpatterns += patterns('',

        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': '%s/../public/media'%settings.PROJECT_ROOT, 'show_indexes': True}),
        )
