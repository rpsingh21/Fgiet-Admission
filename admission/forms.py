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
            'image':'max size of image is 200 KB',
            'signImage':'max size of signater image is 100 KB',
        }

    def clean_aadharNo(self):
        aadharNo = self.cleaned_data['aadharNo']
        if aadharNo.isdigit():
            return aadharNo
        raise forms.ValidationError('Eneter a vaild Aadhar no.')
    
    def clean_mobileNo(self):
        mobileNo = self.cleaned_data['mobileNo']
        if len(mobileNo) ==10 and mobileNo.isdigit():
            return mobileNo
        raise forms.ValidationError('Mobile no. must be contain 10 digite')



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
        help_texts ={
            'highSchoolResultImage':'Image max size is  350 KB',
        }

    def clean_highSchoolRollNo(self):
        highSchoolRollNo = self.cleaned_data['highSchoolRollNo']
        if highSchoolRollNo.isdigit():
            return highSchoolRollNo
        raise forms.ValidationError('Enter valid Roll no.')


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
        help_texts ={
            'intermediateResultImage':'Image max size is 350 KB',
        }

    def clean_intermediateRollNo(self):
        intermediateRollNo = self.cleaned_data['intermediateRollNo']
        if intermediateRollNo.isdigit():
            return intermediateRollNo
        raise forms.ValidationError('Enter valid Roll no.')


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
        help_texts ={
            'ugOrDiplomResultimage':'Image max size is 350 KB',
        }

    def clean_ugOrDiplomRollNo(self):
        ugOrDiplomRollNo = self.cleaned_data['ugOrDiplomRollNo']
        if ugOrDiplomRollNo.isdigit():
            return ugOrDiplomRollNo
        raise forms.ValidationError('Enter valid Roll no.')


class UpseeForm(forms.ModelForm):

    class Meta:
        model = Upsee
        fields = [
            'upseeRollNo',
            'rank',
            'catRank'
        ]
        labels = {
            'rank':'Applicant Upsee Rank',
            'catRank':'Applicant category rank',
            'upseeRollNo':'Applicant Upsee Roll No.'
        }

    def clean_upseeRollNo(self):
        upseeRollNo = self.cleaned_data['upseeRollNo']
        if upseeRollNo.isdigit():
            return upseeRollNo
        raise forms.ValidationError('Enter valid Roll no.')


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

