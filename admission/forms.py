from django import forms

from .models import Candidate, HighSchool, Intermediate, UgOrDiploma, Upsee

class HighSchoolForm(forms.ModelForm):

    class Meta:
        model = HighSchool
        fields = [
            'highSchoolPassingYear',
            'highSchoolBoard',
            'highSchoolPercentageMarks',
            'highSchoolResultImage',
        ]
        labels = {
            'highSchoolPassingYear':'year of passing',
            'highSchoolBoard':'board',
            'highSchoolPercentageMarks':'Percentage Marks',
            'highSchoolResultImage':'upload marksheet photograph',
        }

class IntermediateForm(forms.ModelForm):

    class Meta:
        model = Intermediate
        fields = [
            'intermediatePassingYear',
            'intermediateBoard',
            'intermediatePercentageMarks',
            'intermediateResultImage',
            'math',
            'physics',
            'chemistry'
        ]
        labels = {
            'intermediatePassingYear':'passing of Year',
            'intermediateBoard':'board',
            'intermediatePercentageMarks':'Percentage Marks',
            'intermediateResultImage':'upload marksheet photograph',
            'math':'Percentage marks in Math',
            'physics':'Percentage marks in physics',
            'chemistry':'Percentage marks in chemistry'
        }

class UgOrDiplomaForm(forms.ModelForm):

    class Meta:
        model = UgOrDiploma
        fields = [
            'ugOrDiplompassingYear',
            'ugOrDiplomBoard',
            'ugOrDiplomBranch',
            'ugOrDiplomPercentageMarks',
            'ugOrDiplomResultimage'
        ]
        labels = {
            'ugOrDiplompassingYear':'Passing of year',
            'ugOrDiplomBoard':'Board',
            'ugOrDiplomBranch':'Branch',
            'ugOrDiplomPercentageMarks':'Percentage Marks',
            'ugOrDiplomResultimage':'upload marksheet photograph'
        }

class UpseeForm(forms.ModelForm):

    class Meta:
        model = Upsee
        fields = [
            'rank',
            'catRank',
            'upseeRollNo',
        ]
        labels = {
            'rank':'Upsee Rank',
            'catRank':'category rank',
            'upseeRollNo':'Upsee Roll No.'
        }

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
        labels = {
            "applyYear":"Apply Year",
            "course":"Apply Course",
            "name": "Name Of Applicant",
            "aadharNo" : "Aadhar No of Applicant",
            "fatherName":"father name of Applicant",
            'guardianIncome':'Guardian Income',
            'category':'category',
            'dob':'date of birth',
            'mobileNo':'Mobile No',
            'image':'Upload color Photograph of Applicant ',
            'signImage':'Upload sigature of Applicant',
        }

