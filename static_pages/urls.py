from django.urls import path
from static_pages.views import AboutView


urlpatterns = [
    path('about', AboutView.as_view(), name='about'),
]