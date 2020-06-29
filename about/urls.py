from django.urls import path

from about import views


urlpatterns = [
    path('', views.AboutViewForm.as_view(), name='about'),
]