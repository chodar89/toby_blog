from django.contrib import admin

from .models import Tag, Post

class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag')
    list_per_page = 20
    


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_posted', 'is_featured', 'clap', 'views', 'date')
    list_editable = ('is_posted', 'is_featured')
    list_per_page = 20

admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)