from django.shortcuts import render
from django.http import HttpResponse

from .forms import CandidateForm, UpseeForm, UgOrDiplomaForm, IntermediateForm, HighSchoolForm

def formView(request):
    candidateForm = CandidateForm(request.POST or None, request.FILES or None)
    highSchoolForm = HighSchoolForm(request.POST or None, request.FILES or None)
    intermediateForm = IntermediateForm(request.POST or None, request.FILES or None)
    ugOrDiplomaForm = UgOrDiplomaForm(request.POST or None, request.FILES or None)
    upseeForm = UpseeForm(request.POST or None, request.FILES or None)
    content = {
        'title' : 'Admission Form',
        'candidateForm' : candidateForm,
        'highSchoolForm' : highSchoolForm,
        'intermediateForm' : intermediateForm,
        'ugOrDiplomaForm' : ugOrDiplomaForm,
        'upseeForm' : upseeForm
    }
    if request.method == 'POST':
        if candidateForm.is_valid() and highSchoolForm.is_valid() and intermediateForm.is_valid() and ugOrDiplomaForm.is_valid() and upseeForm.is_valid():    
            instance = candidateForm.save(commit = False)
            instance.highSchoole = highSchoolForm.save()
            instance.intermediate = intermediateForm.save()
            instance.ugOrDiploma = ugOrDiplomaForm.save()
            instance.upsee = upseeForm.save()
            instance.save()
            return render(request,'success.html',{'instance':instance})
    return render(request,'form.html',content)