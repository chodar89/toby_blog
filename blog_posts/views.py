from django.shortcuts import render, get_object_or_404
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
    # queryset = Post.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)