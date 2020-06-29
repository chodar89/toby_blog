from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'email', 'fname', 'date')
    list_per_page = 10

admin.site.register(Contact, ContactAdmin)