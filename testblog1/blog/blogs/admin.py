from django.contrib import admin

from blogs.models import Blog, Post

class BlogsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}
    list_display = ('active', 'name', 'description', 'user')
    list_display_links = ('name',)
    list_editable = ('active',)
    list_filter = ('modified', 'created', 'active')

class PostAdmin(admin.ModelAdmin):
    """docstring for PostAdmin"""
    prepopulated_fields = {"slug": ("title", )}
    list_display = ('active', 'title', 'excerpt', 'publish_at')
    list_display_links = ('title',)
    list_editable = ('active', )
    list_filter = ('publish_at', 'modified', 'created', 'active')
    fieldsets = (
        (None, {
            'fields': ('title', 'blog'),
        }),
        ('Publication', {
            'fields': ('active', 'publish_at'),
            'description': "Control whether or not and when ...",
        }),
        ('Content', {
            'fields': ('excerpt', 'body', 'tags'),
        }),
        ('Optional', {
            'fields': ('slug',),
            'classes': ('collapse',),
        })
    )

admin.site.register(Blog, BlogsAdmin)
admin.site.register(Post, PostAdmin)

