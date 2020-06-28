from django.shortcuts import render, get_object_or_404
from django.views.generic import View, DetailView

from .models import Post, Tag


class BlogView(View):
    """
    Blog posts view
    """
    template_name = 'blog/blog.html'
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        tags = Tag.objects.all().order_by('-views')[:5]
        context = {
            'posts':posts,
            'tags': tags
        }
        return render(request, self.template_name, context)
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
        post = get_object_or_404(Post, id=id_)
        if post:
            for tag in post.tags.all():
                tag.views += 1
                tag.save()
            post.views += 1
            post.save()
        return post