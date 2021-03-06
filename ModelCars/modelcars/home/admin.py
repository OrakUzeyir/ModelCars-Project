from django.contrib import admin

# Register your models here.
from home.models import Settings, ContactFormMessage

class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    list_filter = ['status']

admin.site.register(Settings)
admin.site.register(ContactFormMessage, ContactFormMessageAdmin)