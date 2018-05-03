from django import forms

from .models import (
    Candidate,
    HighSchool,
    Intermediate,
    PCM,
    UgOrDiploma,
    Upsee,
    Branch
)

class CandidateForm(forms.ModelForm):

    class Meta:
        model = Candidate
        fields = [
            'applyYear',
            'course',
            'name',
            'fatherName',
            'gender',
            'aadharNo',
            'email',
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
        help_texts = {
            
        }
    
    # def __init__(self, year, course,*args, **kwargs):
    #     super(CandidateForm, self).__init__( *args, **kwargs)
    #     self.fields['course'] = course
    #     self.fields['applyYear'] = year

class HomeForm(forms.ModelForm):

    class Meta:
        model = Candidate
        fields = [
            'applyYear',
            'course'
        ]
        labels = {
            "applyYear":"Apply Year",
            "course":"Apply Course",
        }

class HighSchoolForm(forms.ModelForm):

    class Meta:
        model = HighSchool
        fields = [
            'highSchoolPassingYear',
            'highSchoolRollNo',
            'highSchoolBoard',
            'highSchoolPercentageMarks',
            'highSchoolResultImage',
        ]
        labels = {
            'highSchoolPassingYear':'year of passing',
            'highSchoolRollNo':'roll no',
            'highSchoolBoard':'board',
            'highSchoolPercentageMarks':'Percentage Marks',
            'highSchoolResultImage':'upload marksheet photograph',
        }

class IntermediateForm(forms.ModelForm):

    class Meta:
        model = Intermediate
        fields = [
            'intermediatePassingYear',
            'intermediateRollNo',
            'intermediateBoard',
            'intermediatePercentageMarks',
            'intermediateResultImage',
        ]
        labels = {
            'intermediatePassingYear':'passing of Year',
            'intermediateRollNo':'Roll no',
            'intermediateBoard':'board',
            'intermediatePercentageMarks':'Percentage Marks',
            'intermediateResultImage':'upload marksheet photograph',
        }
    
class PCMForm(forms.ModelForm):

    class Meta:
        model = PCM
        fields = [
            'math',
            'physics',
            'chemistry',
        ]
        labels = {
            'math':'Percentage marks in Math',
            'physics':'Percentage marks in physics',
            'chemistry':'Percentage marks in chemistry'
        }

class UgOrDiplomaForm(forms.ModelForm):

    class Meta:
        model = UgOrDiploma
        fields = [
            'ugOrDiplompassingYear',
            'ugOrDiplomRollNo',
            'ugOrDiplomBoard',
            'ugOrDiplomBranch',
            'ugOrDiplomPercentageMarks',
            'ugOrDiplomResultimage'
        ]
        labels = {
            'ugOrDiplompassingYear':'Passing of year',
            'ugOrDiplomRollNo':'roll no',
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
            'rank':'Applicant Upsee Rank',
            'catRank':'Applicant category rank',
            'upseeRollNo':'Applicant Upsee Roll No.'
        }

class BranchFrom(forms.ModelForm):

    class Meta:
        model = Branch
        fields = [
            'first',
            'second',
            'third',
            'fourth'
        ]
        labels = {
            'first':'first prefrance',
            'second':'second prefrance',
            'third':'third prefrance',
            'fourth':'fourth prefrance'
        }

