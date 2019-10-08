from django import forms
from django.conf import settings
from django.template.defaultfilters import filesizeformat

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
            'dob': forms.DateInput(attrs={'class': 'datepicker'}),
        }
        labels = {
            "applyYear": "Apply Year",
            "course": "Apply Course",
            "name": "Name",
            "aadharNo": "Aadhar Number ",
            "fatherName": "Father's Name",
            'guardianIncome': 'Guardian Income',
            'category': 'Category',
            'dob': 'Date of Birth',
            'mobileNo': 'Mobile No',
            'image': 'Upload Scanned Photograph of Candidate',
            'signImage': 'Upload Scanned Sigature',
        }
        help_texts = {
            'image': 'max size is 100 KB',
            'signImage': 'max size of is 100 KB',
            'dob': 'mm/dd/yyyy'
        }

    def clean_aadharNo(self):
        aadharNo = self.cleaned_data['aadharNo']
        if aadharNo.isdigit():
            return aadharNo
        raise forms.ValidationError('Eneter a vaild Aadhar no.')

    def clean_mobileNo(self):
        mobileNo = self.cleaned_data['mobileNo']
        if len(mobileNo) == 10 and mobileNo.isdigit():
            return mobileNo
        raise forms.ValidationError('Mobile no. must be contain 10 digite')

    def clean_signImage(self):
        signImage = self.cleaned_data['signImage']
        size = getattr(signImage, '_size', 0)
        if size > settings.MAX_UPLOAD_SIZE:
            raise forms.ValidationError("Please keep image size under %s. Current filesize %s" % (
                filesizeformat(settings.MAX_UPLOAD_SIZE//2), filesizeformat(size)))
        return signImage

    def clean_image(self):
        image = self.cleaned_data['image']
        size = getattr(image, '_size', 0)
        if size > settings.MAX_UPLOAD_SIZE:
            raise forms.ValidationError("Please keep image size under %s. Current filesize %s" % (
                filesizeformat(settings.MAX_UPLOAD_SIZE//2), filesizeformat(size)))
        return image


class HomeForm(forms.ModelForm):

    class Meta:
        model = Candidate
        fields = [
            'applyYear',
            'course'
        ]
        labels = {
            "applyYear": "Apply Year",
            "course": "Apply Course",
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
            'highSchoolPassingYear': 'Passing Year',
            'highSchoolRollNo': 'Roll No',
            'highSchoolBoard': 'Board',
            'highSchoolPercentageMarks': 'Percentage Marks',
            'highSchoolResultImage': 'Upload Scanned Marksheet',
        }
        help_texts = {
            'highSchoolResultImage': 'max size is  200 KB',
        }

    def clean_highSchoolResultImage(self):
        image = self.cleaned_data['highSchoolResultImage']
        size = getattr(image, '_size', 0)
        if size > settings.MAX_UPLOAD_SIZE:
            raise forms.ValidationError(
                "Please keep image size under %s. Current filesize %s" % (
                    filesizeformat(settings.MAX_UPLOAD_SIZE),
                    filesizeformat(size))
            )
        return image

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
            'intermediatePassingYear': 'Passing Year',
            'intermediateRollNo': 'Roll No',
            'intermediateBoard': 'Board',
            'intermediatePercentageMarks': 'Percentage Marks',
            'intermediateResultImage': 'Upload scanned Marksheet',
        }
        help_texts = {
            'intermediateResultImage': 'max size is 200 KB',
        }

    def clean_intermediateRollNo(self):
        intermediateRollNo = self.cleaned_data['intermediateRollNo']
        if intermediateRollNo.isdigit():
            return intermediateRollNo
        raise forms.ValidationError('Enter valid Roll no.')

    def clean_intermediateResultImage(self):
        image = self.cleaned_data['intermediateResultImage']
        size = getattr(image, '_size', 0)
        if size > settings.MAX_UPLOAD_SIZE:
            raise forms.ValidationError(
                "Please keep image size under %s. Current filesize %s" % (
                    filesizeformat(settings.MAX_UPLOAD_SIZE),
                    filesizeformat(size)))
        return image


class PCMForm(forms.ModelForm):

    class Meta:
        model = PCM
        fields = [
            'math',
            'physics',
            'chemistry',
        ]
        labels = {
            'math': 'Marks in Math',
            'physics': 'Marks in Physics',
            'chemistry': 'marks in Chemistry'
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
            'ugOrDiplompassingYear': 'Passing year',
            'ugOrDiplomRollNo': 'Roll No',
            'ugOrDiplomBoard': 'Board',
            'ugOrDiplomBranch': 'Branch',
            'ugOrDiplomPercentageMarks': 'Percentage Marks',
            'ugOrDiplomResultimage': 'Upload Scanned Marksheet'
        }
        help_texts = {
            'ugOrDiplomResultimage': 'max size is 200 KB',
            'ugOrDiplomPercentageMarks': 'If your final result is not \
                announced then you fill last two-year average Details.'
        }

    def clean_ugOrDiplomResultimage(self):
        image = self.cleaned_data['ugOrDiplomResultimage']
        size = getattr(image, '_size', 0)
        if size > settings.MAX_UPLOAD_SIZE:
            raise forms.ValidationError(
                "Please keep resume size under %s. Current filesize %s" % (
                    filesizeformat(settings.MAX_UPLOAD_SIZE),
                    filesizeformat(size)))
        return image

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
            'rank': 'Upsee Rank',
            'catRank': 'Category Rank',
            'upseeRollNo': 'Upsee Roll No.'
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
            'first': 'First Prefrance',
            'second': 'Second Prefrance',
            'third': 'Third Prefrance',
            'fourth': 'Fourth Prefrance'
        }
