from django.contrib import admin

from .models import (
    HighSchool,
    Intermediate,
    Upsee, Candidate,
    UgOrDiploma,
    Branch,
    PCM
)


class CandidateModelAdmin(admin.ModelAdmin):
    list_display = ['registrationNo', 'name', 'applyYear', 'aadharNo',
                    'fatherName', 'mobileNo', 'category', 'address', 'course']
    search_fields = ['registrationNo', 'name', 'fatherName', 'address']


class HighSchoolModelAdmin(admin.ModelAdmin):
    list_display = ['candidate', 'highSchoolPassingYear',
                    'highSchoolBoard', 'highSchoolRollNo',
                    'highSchoolPercentageMarks']
    search_fields = ['highSchoolPassingYear', 'highSchoolBoard',
                     'highSchoolRollNo', 'highSchoolPercentageMarks']


class IntermediateModelAdmin(admin.ModelAdmin):
    list_display = ['candidate', 'intermediatePassingYear',
                    'intermediateBoard', 'intermediateRollNo',
                    'intermediatePercentageMarks']
    search_fields = ['intermediatePassingYear',
                     'intermediateBoard', 'intermediateRollNo', ]


class PCMModelAdmin(admin.ModelAdmin):
    list_display = ['intermediate', 'math', 'physics', 'chemistry']
    search_fields = ['math', 'physics', 'chemistry']


class UgOrDiplomaModelAdmin(admin.ModelAdmin):
    list_display = ['candidate', 'ugOrDiplompassingYear', 'ugOrDiplomBoard',
                    'ugOrDiplomRollNo', 'ugOrDiplomBranch',
                    'ugOrDiplomPercentageMarks']
    search_fields = ['ugOrDiplompassingYear', 'ugOrDiplomBoard',
                     'ugOrDiplomRollNo', 'ugOrDiplomBranch',
                     'ugOrDiplomPercentageMarks']


class UpseeModelAdmin(admin.ModelAdmin):
    list_display = ['candidate', 'rank', 'catRank', 'upseeRollNo']
    search_fields = ['rank', 'catRank', 'upseeRollNo']


class BranchModelAdmin(admin.ModelAdmin):
    list_display = ['candidate', 'first', 'second', 'third', 'fourth']


admin.site.register(Candidate, CandidateModelAdmin)
admin.site.register(HighSchool, HighSchoolModelAdmin)
admin.site.register(Intermediate, IntermediateModelAdmin)
admin.site.register(PCM, PCMModelAdmin)
admin.site.register(UgOrDiploma, UgOrDiplomaModelAdmin)
admin.site.register(Upsee, UpseeModelAdmin)
admin.site.register(Branch, BranchModelAdmin)
