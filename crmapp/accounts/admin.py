from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'uuid', 'owner')

admin.site.register(Account, AccountAdmin)
