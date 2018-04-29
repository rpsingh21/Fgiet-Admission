from django.contrib import admin
from .models import Profile

class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['user','phone','branch']
    search_fields = ['user','phone','branch']

admin.site.register(Profile, ProfileModelAdmin)
