from django.shortcuts import render
from django.views.generic import View, DetailView

from .models import Post


class BlogView(View):
    """
    Blog posts view
    """
    template_name = 'blog/blog.html'
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        return render(request, self.template_name, {'posts':posts})
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class BlogPostView(DetailView):
    """
    Blog post view
    """
    template_name = 'blog/blog_post.html'