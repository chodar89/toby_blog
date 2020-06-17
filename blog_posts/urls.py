from django.urls import path

from blog_posts.views import BlogView

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
]