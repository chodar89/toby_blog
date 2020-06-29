from django.urls import path

from .views import ThankYouView

urlpatterns = [
    path('thankyou', ThankYouView.as_view(), name='thank_you'),
]