from django.shortcuts import render
from django.views.generic import TemplateView


class BlogView(TemplateView):
    """
    Blog posts view
    """
    template_name = 'blog/blog.html'


class BlogPostView(TemplateView):
    """
    Blog post view
    """
    template_name = 'blog/blog_post.html'