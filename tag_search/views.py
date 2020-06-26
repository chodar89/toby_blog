from django.shortcuts import render
from django.views.generic import View

from blog_posts.models import Post, Tag

# Create your views here.

class SearchView(View):
    template_name = 'tag_search/blog_tag.html'

    def get(self, request, *args, **kwargs):
        tag_name = self.kwargs.get("tag")
        posts = Post.objects.filter(tags__tag=tag_name)
        tags = Tag.objects.all().order_by('views')[:5]
        context = {
            'posts':posts,
            'tags': tags
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        search_tag = self.request.POST.get("tag", None)
        tags = Tag.objects.all().order_by('views')[:5]
        if search_tag is not None:
            print(search_tag)
            posts = Post.objects.filter(tags__tag=search_tag.lower())
        context = {
            'posts':posts,
            'tags': tags
        }
        return render(request, self.template_name, context)