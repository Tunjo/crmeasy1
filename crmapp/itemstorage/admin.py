from django.contrib import admin
from .models import ItemStorage


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'choice', 'created_on')


admin.site.register(ItemStorage, ItemAdmin)