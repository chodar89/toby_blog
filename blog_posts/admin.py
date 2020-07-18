from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Tag, Post


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'views')
    list_per_page = 20
    


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content', 'source')
    list_display = ('title', 'is_posted', 'is_featured', 'claps', 'views', 'date')
    list_editable = ('is_posted', 'is_featured')
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 20

admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)