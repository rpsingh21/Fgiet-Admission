from django.contrib import admin
from django.db import models

from pagedown.widgets import AdminPagedownWidget

from .models import Profile, SiteContent

class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['user','phone','branch']
    search_fields = ['user','phone','branch']

class SiteContentAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

admin.site.register(Profile, ProfileModelAdmin)
admin.site.register(SiteContent, SiteContentAdmin)
