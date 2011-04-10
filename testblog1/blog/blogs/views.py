from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from blogs.models import Blogs, Post


def blog_index(request):
    """docstring for blog_index"""
    blogs = Blogs.objects.filter(active=True)

    return render_to_response('index.html', {
        'blogs': blogs,
    }, context_instance=RequestContext(request))

def blog(request, slug):
    """docstring for blog"""
    blog = get_object_or_404(Blogs, active=True, slug=slug)

    return render_to_response('blog/index.html', {
        'blog': blog
        }, context_instance=RequestContext(request))
