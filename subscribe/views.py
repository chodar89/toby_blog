from django.shortcuts import render, reverse
from django.views.generic import CreateView

from .forms import SubscribeForm
# Create your views here.

class SubscribeView(CreateView):
    template_name = 'subscribe/subscribe.html'
    form_class = SubscribeForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('thank_you_sub')