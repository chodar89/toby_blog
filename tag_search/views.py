from django.shortcuts import render
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator

from blog_posts.models import Post, Tag

# Create your views here.

class SearchView(View):
    """
    View that renders posts related
    to user tag search or tag click/link
    """
    template_name = 'tag_search/blog_tag.html'

    def get(self, request, *args, **kwargs):
        tag_name = self.kwargs.get("tag")
        posts = Post.objects.filter(tags__tag=tag_name).order_by('-date')
        # Try to update tag view and filter posts with tag from search form
        try:
            get_tag = Tag.objects.get(tag=tag_name)
            get_tag.views += 1
            get_tag.save()
        except ObjectDoesNotExist:
            pass
        # Get 5 most popular tags
        tags = Tag.objects.all().order_by('-views')[:5]
        # Get all tags
        all_tags = Tag.objects.all().order_by('tag')
        # Set number of posts to dipslay on one page
        paginator = Paginator(posts, 5)
        page_number = request.GET.get('page')
        page_posts = paginator.get_page(page_number)
        context = {
            'page_posts':page_posts,
            'tags': tags,
            'all_tags': all_tags
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """
        Post view handle tag search form
        """
        search_tag = self.request.POST.get("tag", None)
        search_tag = search_tag.lower()
        if search_tag is not None:
            # Try to update tag view and filter posts with tag from search form
            try:
                get_tag = Tag.objects.get(tag=search_tag)
                get_tag.views += 1
                get_tag.save()
            except ObjectDoesNotExist:
                pass
            posts = Post.objects.filter(tags__tag=search_tag).order_by('-date')
        else:
            posts = []
        # Get 5 most popular tags
        tags = Tag.objects.all().order_by('-views')[:5]
        # Get all tags
        all_tags = Tag.objects.all().order_by('tag')
        # Set number of posts to dipslay on one page
        paginator = Paginator(posts, 5)
        page_number = request.GET.get('page')
        page_posts = paginator.get_page(page_number)
        context = {
            'page_posts':page_posts,
            'tags': tags,
            'all_tags': all_tags
        }
        return render(request, self.template_name, context)
