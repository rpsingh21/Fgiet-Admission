from django.contrib import admin

from .models import HighSchool, Intermediate, Upsee, Candidate, UgOrDiploma, Branch

class CandidateModelAdmin(admin.ModelAdmin):
    list_display = ['registrationNo','name','applyYear','aadharNo','fatherName','mobileNo','category','address','course']
    search_fields = ['registrationNo','name','fatherName','address']

class HighSchoolModelAdmin(admin.ModelAdmin):
    list_display = ['highSchoolPassingYear','highSchoolBoard','highSchoolRollNo','highSchoolPercentageMarks']
    search_fields = ['highSchoolPassingYear','highSchoolBoard','highSchoolRollNo','highSchoolPercentageMarks']

class IntermediateModelAdmin(admin.ModelAdmin):
    list_display = ['intermediatePassingYear','intermediateBoard','intermediateRollNo','intermediatePercentageMarks','math','physics','chemistry']
    search_fields = ['intermediatePassingYear','intermediateBoard','intermediateRollNo',]

class UgOrDiplomaModelAdmin(admin.ModelAdmin):
    list_display = ['ugOrDiplompassingYear','ugOrDiplomBoard','ugOrDiplomRollNo','ugOrDiplomBranch','ugOrDiplomPercentageMarks']
    search_fields = ['ugOrDiplompassingYear','ugOrDiplomBoard','ugOrDiplomRollNo','ugOrDiplomBranch','ugOrDiplomPercentageMarks']

class UpseeModelAdmin(admin.ModelAdmin):
    list_display = ['rank','catRank','upseeRollNo']
    search_fields = ['rank','catRank','upseeRollNo']

class BranchModelAdmin(admin.ModelAdmin):
    list_display = ['first', 'second', 'third', 'fourth']

admin.site.register(HighSchool, HighSchoolModelAdmin)
admin.site.register(Intermediate, IntermediateModelAdmin)
admin.site.register(UgOrDiploma, UgOrDiplomaModelAdmin)
admin.site.register(Upsee, UpseeModelAdmin)
admin.site.register(Branch, BranchModelAdmin)
admin.site.register(Candidate, CandidateModelAdmin)
