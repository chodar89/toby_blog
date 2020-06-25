from django.db import models

# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=20)

    class Meta:
        ordering = ['tag']
    
    def __str__(self):
        return self.tag


class Post(models.Model):
    title = models.CharField(max_length=30, blank=False)
    description = models.CharField(max_length=350, blank=False)
    is_featured = models.BooleanField(default=False)
    is_posted = models.BooleanField(default=False)
    text = models.TextField()
    tags = models.ManyToManyField(Tag)
    clap = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    read_time = models.PositiveIntegerField(blank=False)
    img_main = models.ImageField(upload_to='imgs/post/%Y/%m/%d')
    img_1 = models.ImageField(upload_to='imgs/post/%Y/%m/%d', blank=True)
    img_2 = models.ImageField(upload_to='imgs/post/%Y/%m/%d', blank=True)
    img_3 = models.ImageField(upload_to='imgs/post/%Y/%m/%d', blank=True)
    img_4 = models.ImageField(upload_to='imgs/post/%Y/%m/%d', blank=True)
    img_5 = models.ImageField(upload_to='imgs/post/%Y/%m/%d', blank=True)
    img_6 = models.ImageField(upload_to='imgs/post/%Y/%m/%d', blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title

