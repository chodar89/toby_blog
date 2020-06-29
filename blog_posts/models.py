from django.db import models
from django.urls import reverse
import datetime

# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=20)
    views = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['tag']
    
    def __str__(self):
        return self.tag


class Post(models.Model):
    title = models.CharField(max_length=30, blank=False)
    header = models.CharField(max_length=150, blank=True)
    description = models.CharField(max_length=350, blank=False)
    is_featured = models.BooleanField(default=False)
    is_posted = models.BooleanField(default=False)
    content = models.TextField()
    source = models.TextField()
    tags = models.ManyToManyField(Tag)
    claps = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    read_time = models.PositiveIntegerField(blank=False)
    img_main = models.ImageField(upload_to='imgs/post/%Y/%m/%d')
    img_1 = models.ImageField(upload_to='imgs/post/%Y/%m/%d', blank=True)
    img_2 = models.ImageField(upload_to='imgs/post/%Y/%m/%d', blank=True)
    img_3 = models.ImageField(upload_to='imgs/post/%Y/%m/%d', blank=True)
    img_4 = models.ImageField(upload_to='imgs/post/%Y/%m/%d', blank=True)
    img_5 = models.ImageField(upload_to='imgs/post/%Y/%m/%d', blank=True)
    img_6 = models.ImageField(upload_to='imgs/post/%Y/%m/%d', blank=True)
    date = models.DateTimeField(auto_now_add=False, blank=True, default=datetime.datetime.now)

    def get_absolute_url(self):
        return reverse('blog_post', kwargs={'id': self.id})

    def get_clap_url(self):
        return reverse('clap', kwargs={'id': self.id})
    
    def get_clap_api_url(self):
        return reverse('clap_api', kwargs={'id': self.id})

    def __str__(self):
        return self.title

