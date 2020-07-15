from django.shortcuts import render, reverse, redirect
from django.views.generic import CreateView
from django.contrib import messages
from django.conf import settings

from .models import Subscribe
from .forms import SubscribeForm

import json
import requests

MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY
MAILCHIMP_DATA_CENTER = settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_EMAIL_LIST_ID = settings.MAILCHIMP_EMAIL_LIST_ID

api_url = f'https://{MAILCHIMP_DATA_CENTER}.api.mailchimp.com/3.0'
members_endpoint = f'{api_url}/lists/{MAILCHIMP_EMAIL_LIST_ID}/members'

def subscribe(email):
    data = {
        "email_address": email,
        "status": "subscribed"
    }
    r = requests.post(
        members_endpoint,
        auth=("", MAILCHIMP_API_KEY),
        data = json.dumps(data)
    )
    return r.status_code, r.json()


class SubscribeView(CreateView):
    template_name = 'subscribe/subscribe.html'
    form_class = SubscribeForm

    def form_valid(self, form):
        # email_subscribe_q = Subscribe.objects.filter(email = form.instance.email)
        # if email_subscribe_q.exists():
        #     messages.info(self.request, "You are already subscribed")
        #     return redirect('subscribe')
        # else:
        subscribe(form.instance.email)
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('thank_you_sub')