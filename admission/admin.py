from django.contrib import admin

from .models import HighSchool, Intermediate, Upsee, Candidate

class CandidateModelAdmin(admin.ModelAdmin):
    list_display = ['name','applyYear','aadharNo','fatherName','mobileNo','category','address','course']
    search_fields = ['name','address']

admin.site.register(HighSchool)
admin.site.register(Intermediate)
admin.site.register(Upsee)
admin.site.register(Candidate, CandidateModelAdmin)

