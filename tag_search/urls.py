from django.urls import path

from .views import SearchView

urlpatterns = [
    path('<str:tag>', SearchView.as_view(), name='tag_search'),
]