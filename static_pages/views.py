from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class AboutView(TemplateView):
    """
    Static about page
    """
    template_name = 'about.html'
