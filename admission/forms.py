from django import forms

from .models import Candidate, HighSchool, Intermediate, UgOrDiploma, Upsee

class HighSchoolForm(forms.ModelForm):

    class Meta:
        model = HighSchool
        fields = [
            'passingYear',
            'board',
            'percentageMarks',
            'highResultImage',
        ]

class IntermediateForm(forms.ModelForm):

    class Meta:
        model = Intermediate
        fields = [
            'passingYear',
            'board',
            'percentageMarks',
            'intermeduateResultImage',
            'math',
            'physics',
            'chemistry'
        ]

class UgOrDiplomaForm(forms.ModelForm):

    class Meta:
        model = UgOrDiploma
        fields = [
            'passingYear',
            'board',
            'percentageMarks',
            'ugOrDiplomaResultimage',
            'branch'
        ]

class UpseeForm(forms.ModelForm):

    class Meta:
        model = Upsee
        fields = [
            'rank',
            'catRank',
            'upseeRollNo',
        ]

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = [
            'applyYear',
            'course',
            'name',
            'aadharNo',
            'fatherName',
            'guardianIncome',
            'category',
            'dob',
            'address',
            'mobileNo',
            'image',
            'signImage',
        ]
        widgets = {
            'dob': forms.DateInput(attrs={'class':'datepicker'}),
        }
