from django.urls import path

from .views import AboutViewForm


urlpatterns = [
    path('', AboutViewForm.as_view(), name='about'),
]