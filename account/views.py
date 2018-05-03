from django.contrib.auth.decorators import login_required
from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, reverse

from .forms import LoginForm
from admission.models import Candidate

def login_view(request):
    form = LoginForm(request.POST or None)
    next = request.GET.get('next')
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            login(request, user)
            if next:
                return redirect(next)
            return redirect("/account")
    next = request.META.get('HTTP_REFERER')
    return render(request, "account/loginForm.html", {"title": "Admin Login", "form": form})

@login_required(login_url='/account/login/')
def adminTableView(request):
    instances = Candidate.objects.all().order_by('-timeStamp')
    if not request.user.is_superuser:
        if not request.user.profile.branch:
            raise PermissionDenied
        print(request.user.profile.branch)
        instances = instances.filter(course=request.user.profile.branch)
    return render(request, 'account/table.html',{'instances':instances})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))