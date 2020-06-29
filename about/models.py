from django.db import models
from django.utils import timezone

# Create your models here.


class Contact(models.Model):
    fname = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    subject = models.CharField(max_length=40, blank=False, null=False)
    message = models.TextField(max_length=1500, blank=False, null=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.subject