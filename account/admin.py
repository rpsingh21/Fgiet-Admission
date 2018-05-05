from django.contrib import admin
from .models import Profile, SiteContent

class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['user','phone','branch']
    search_fields = ['user','phone','branch']

admin.site.register(Profile, ProfileModelAdmin)
admin.site.register(SiteContent)
