from django.shortcuts import render, get_object_or_404
from django.views.generic import View, DetailView, RedirectView
from django.http import JsonResponse

from .models import Post, Tag


class BlogView(View):
    """
    Blog posts view. Get all posts and render.
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
    Blog post view, get post and update tag and post views or 404
    """
    template_name = 'blog/blog_post.html'

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


class PostClapView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        id_ = self.kwargs.get("id")
        obj = get_object_or_404(Post, id=id_)
        url_ = obj.get_absolute_url()
        obj.claps += 1
        obj.save()
        return url_