from django.urls import path

from blog_posts.views import BlogView, BlogPostView

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('post/<int:id>/', BlogPostView.as_view(), name='blog_post'),
]