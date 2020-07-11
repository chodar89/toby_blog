from django.urls import path

from .views import BlogView, BlogPostView, PostClapAPI

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('post/<int:id>/', BlogPostView.as_view(), name='blog_post'),
    path('post/<int:id>/clap/', PostClapView.as_view(), name='clap'),
    path('api/post/<int:id>/clap/', PostClapAPI.as_view(), name='clap_api'),
]