from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404

from .forms import (
    CandidateForm,
    UpseeForm,
    UgOrDiplomaForm,
    IntermediateForm,
    HighSchoolForm
)
from .models import Candidate

def form_view(request):
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
            request.session['pk'] = instance.id
            request.session['aadhar'] = instance.aadharNo
            return redirect(reverse('admission:success'))
    return render(request,'form.html',content)

def success_view(request):
    if 'pk' not in request.session:
        raise Http404()
    instance = get_object_or_404(Candidate,pk=request.session['pk'])
    return render(request,'success.html',{'instance':instance,'applicant':True})

@login_required(login_url='/account/login/')
def application_view(request,id):
    instance = get_object_or_404(Candidate,id=id)
    if not request.user.is_superuser:
        if request.user.profile.branch != instance.course:
            return HttpResponse("User is not vaild to access this application details")
    return render(request,'success.html',{'instance':instance})

def fqs_view(request):
    return HttpResponse("fqs")