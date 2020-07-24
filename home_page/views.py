from django.shortcuts import render
from django.views.generic import View

from blog_posts.models import Post

# Create your views here.


class HomeView(View):
    """
    Home page view. Get one fatured post and two lates posts and render.
    """
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        featured_post = Post.objects.filter(is_posted=True).filter(is_featured=True).order_by('-date')[:1]
        latest_posts = Post.objects.filter(is_posted=True).order_by('-date')[:2]
        context = {
            'featured_post': featured_post,
            'latest_posts': latest_posts
        }
        return render(request, self.template_name, context)