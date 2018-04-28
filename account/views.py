from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse

from .forms import LoginForm

from admission.models import Candidate

# Create your views here.

def adminTableView(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('account:login'))
    instances = Candidate.objects.all().order_by('-timeStamp')
    return render(request, 'account/table.html',{'instances':instances})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/account")
    next = request.META.get('HTTP_REFERER')
    return render(request, "account/loginForm.html", {"title": "Login", "form": form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))