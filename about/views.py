from django.shortcuts import render
from django.views.generic import CreateView

from about import views

from .forms import ContactForm


# Create your views here.

class AboutViewForm(CreateView):
    """
    About page
    """
    template_name = 'about.html'
    form_class = ContactForm
    success_url = '/about'
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
 