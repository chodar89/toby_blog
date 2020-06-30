from django.db import models
from django.utils import timezone

# Create your models here.

class Subscribe(models.Model):
    email = models.EmailField(blank=False, null=False)
    date = models.DateTimeField(blank=False, default=timezone.now)

    def __str__(self):
        return self.email
