from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class AboutView(View):
    """
    About page
    """
    template_name = 'about.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        
        return render(request, self.template_name, {})