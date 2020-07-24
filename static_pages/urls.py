from django.urls import path

from .views import ThankYouView, ThankYouSubscribeView

urlpatterns = [
    path('thankyou', ThankYouView.as_view(), name='thank_you'),
    path('thankyousub', ThankYouSubscribeView.as_view(), name='thank_you_sub'),
]