from django.shortcuts import render, reverse
from django.views.generic import CreateView


from .forms import ContactForm


# Create your views here.

class AboutViewForm(CreateView):
    """
    About page
    """
    template_name = 'about.html'
    form_class = ContactForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('thank_you')
 