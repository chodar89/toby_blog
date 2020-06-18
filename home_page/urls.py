from django.urls import path

from home_page.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
]