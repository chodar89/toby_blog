from django.shortcuts import render
from django.views.generic import View

from blog_posts.models import Post, Tag

# Create your views here.

class SearchView(View):
    template_name = 'tag_search/blog_tag.html'

    def get(self, request, *args, **kwargs):
        tags = Tag.objects.all().order_by('views')[:5]
        context = {
            'posts':posts,
            'tags': tags
        }
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context)