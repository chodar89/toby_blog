from django.contrib import admin
from .models import Subscribe

# Register your models here.
class SubscribeAdmin(admin.ModelAdmin):
   list_display = ('id', 'email', 'date')
   list_per_page = 20

admin.site.register(Subscribe, SubscribeAdmin)