from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404

from .forms import (
    HomeForm,
    CandidateForm,
    UpseeForm,
    UgOrDiplomaForm,
    IntermediateForm,
    PCMForm,
    HighSchoolForm,
    BranchFrom
)
from .models import Candidate
from account.models import SiteContent
from utils.tasks import send_sms, convert_thumbnail, send_email

def home_view(request):
    homeForm = HomeForm(request.POST or None)
    if request.method == 'POST':
        if homeForm.is_valid():
            year = request.POST.get('applyYear')
            course = request.POST.get('course')
            return redirect(reverse('admission:form',kwargs={'year':year,'course':course}))
    siteContent = SiteContent.objects.filter(name='notice_admission').first()
    content = {
        'title': 'Home',
        'siteContent':siteContent.content,
        'homeForm' : homeForm
    }
    return render(request, 'home.html', content)

def save_with_key(formValue, key):
    temp = formValue.save(commit=False)
    temp.candidate = key
    temp.save()
    return temp

def form_view(request,year,course):
    candidateForm = CandidateForm(request.POST or None, request.FILES or None)
    highSchoolForm = HighSchoolForm(request.POST or None, request.FILES or None)
    intermediateForm = IntermediateForm(request.POST or None, request.FILES or None)
    pcmForm = PCMForm(request.POST or None)
    ugOrDiplomaForm = UgOrDiplomaForm(request.POST or None, request.FILES or None)
    upseeForm = UpseeForm(request.POST or None, request.FILES or None)
    branchFrom = BranchFrom(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        # checking vaildtion
        vaild = True
        if not (candidateForm.is_valid() and highSchoolForm.is_valid() and upseeForm.is_valid):
            vaild = False
        if not year=='2' and course=='BTech':
            if not intermediateForm.is_valid():
                vaild = False
        if not course == 'MCA':
            if not branchFrom.is_valid():
                vaild = False
        if year=='1' and course=='BTech':
            if not pcmForm.is_valid():
                vaild = False
        else:
            if not ugOrDiplomaForm.is_valid():
                vaild = False
        if vaild:
            instance = candidateForm.save()
            instance.registrationNo = "18187"+"{:03}".format(instance.id)
            instance.save()
            save_with_key(highSchoolForm, instance)
            save_with_key(upseeForm, instance)
            temp = None
            if not (course == 'BTech' and year == '2'):
                temp = save_with_key(intermediateForm, instance)
                if course == 'BTech' and year == '1':
                    pcm = pcmForm.save(commit=False)
                    pcm.intermediate = temp
                    pcm.save()
            if not (course == 'BTech' and year == '1'):
                save_with_key(ugOrDiplomaForm, instance)
            if course == 'BTech':
                save_with_key(branchFrom, instance)

            # sending sms and email to user
            mgs ="Congratulation! "+instance.name+", Your registration is successfully completed and Registration No is: "+instance.registrationNo+" For more Information visite website www.fgiet.ac.in ..."
            send_sms.delay(instance.mobileNo,mgs[:139])
            convert_thumbnail.delay(instance.image.path, (420,560))
            convert_thumbnail.delay(instance.signImage.path,(560, 160))
            mail_context = {
                'name':instance.name,
                'registrationNo':instance.registrationNo
            }
            send_email.delay('FGIET Adnission registration','', 'mails/success_mail.html', mail_context,None,[instance.email])

            # return responce 
            request.session['pk'] = instance.id
            request.session['aadhar'] = instance.aadharNo
            return redirect(reverse('admission:success'))
    content = {
        'title' : 'Admission Form',
        'candidateForm' : candidateForm,
        'highSchoolForm' : highSchoolForm,
        'intermediateForm' : intermediateForm,
        'pcmForm' : pcmForm,
        'ugOrDiplomaForm' : ugOrDiplomaForm,
        'upseeForm' : upseeForm,
        'branchFrom':branchFrom,
        'type':{
            'year':year,
            'course':course
        }
    }
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
