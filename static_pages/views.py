from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class ThankYouView(TemplateView):
    template_name = 'static_pages/thankyou.html'

class ThankYouSubscribeView(TemplateView):
    template_name = 'static_pages/thankyou.html'
    