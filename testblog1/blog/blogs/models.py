import datetime

from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

class PostManager(models.Manager):
    """docstring for PostManager"""
    def get_visible(self):
        """docstring for get_visible"""
        return self.get_query_set().filter(publish_at__lte=datetime.datetime.now(), active = True)

class TimeStampedActivate(models.Model):
    """docstring for TimeStamp"""
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False,
                                help_text='Controls whether or not this item is live to the world')

    class Meta:
        abstract = True

class Blog(TimeStampedActivate):
    """
    A blog belonginm to a user
    Blog have multiple posts and one user can have many blog.

    >>> b = Blog()
    >>> b.name = 'Foo Blog'
    >>> b.user = User.objects.create(username = 'foo', password='test')
    >>> b.slug = 'foo-blog'
    >>> b.save()
    >>> print b
    Foo Blog
    >>> print b.user.username
    foo
    """
    name = models.CharField(max_length=255,
                           help_text='Name of your blog. can be anything up to 255 charactersr')
    slug = models.SlugField()
    description = models.TextField(blank=True,
                                  help_text='Describe your blog.')
    user = models.ForeignKey(User, related_name='blog')

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        """docstring for get_absolute_url"""
        return ('blog', (), {
            'slug': self.slug
            })

class Post(TimeStampedActivate):
    """docstring for post
    A post that belongs to a blog.
    >>> b = Blog.objects.get(id=1)
    >>> p = Post()
    >>> p.title = 'A Test Post'
    >>> p.blog = b
    >>> p.body = "Just a small test"
    >>> p.slug = 'a-test-post'
    >>> p.save()
    >>> print p.blog.name
    Foo Blog
    >>> print p.active
    False

    """
    title = models.CharField(max_length=255,
                            help_text="Title of the post. Can be anything up to 255 characters.")
    slug = models.SlugField()
    excerpt = models.TextField(blank=True,
                              help_text='A small teaser of your content')
    body = models.TextField()
    publish_at = models.DateTimeField(default=datetime.datetime.now(),
                                     help_text='Date and time post should become visible.')
    blog = models.ForeignKey(Blog, related_name='posts')
    tags = TaggableManager()
    objects = PostManager()

    def __unicode__(self):
        return self.title

    def is_visible(self):
        """docstring for is_visible
        Checks to see if a post is supposed be visible when accessed outside
        of a queryset.
        """
        if self.active and self.publish_at <= datetime.datetime.now():
            return True
        return False

    @models.permalink
    def get_absolute_url(self):
        return ('post', (), {
            'blog': self.blog.slug,
            'slug': self.slug
            })

    class Meta:
        ordering = [ '-publish_at', '-modified', '-created']


