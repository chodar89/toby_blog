from django.db import models

# Create your models here.


class Contact(models.Model):
    subject = models.CharField(max_length=40, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    fname = models.CharField(max_length=20, blank=False, null=False)
    message = models.CharField(max_length=1500, blank=False, null=False)

    def __str__(self):
        return self.subject