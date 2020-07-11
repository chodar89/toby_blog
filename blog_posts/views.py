from django.shortcuts import render, get_object_or_404
from django.views.generic import View, DetailView, RedirectView
from django.http import JsonResponse
from django.core.paginator import Paginator

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from .models import Post, Tag


class BlogView(View):
    """
    Blog posts view. Get all posts and render.
    """
    template_name = 'blog/blog.html'
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-date')
        tags = Tag.objects.all().order_by('-views')[:5]
        # Set number of posts to dipslay on one page
        paginator = Paginator(posts, 5)
        page_number = request.GET.get('page')
        page_posts = paginator.get_page(page_number)
        context = {
            'page_posts':page_posts,
            'tags': tags
        }
        return render(request, self.template_name, context)


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


class PostClapAPI(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, id=None, format=None):
        obj = get_object_or_404(Post, id=id)
        url_ = obj.get_absolute_url()
        obj.claps += 1
        obj.save()
        data = {
            'claps': obj.claps,
        }
        return Response(data)