from django.urls import path

from .views import BlogView, BlogPostView, PostClapView

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('post/<int:id>/', BlogPostView.as_view(), name='blog_post'),
    path('post/<int:id>/clap/', PostClapView.as_view(), name='clap'),
]