from django.shortcuts import render
from django.views.generic import TemplateView


class BlogView(TemplateView):
    """
    Blog posts view
    """
    template_name = 'blog/blog.html'
    def get(self, request, *args, **kwargs):
       return render(request, self.template_name)

