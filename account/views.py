from django.shortcuts import render

from admission.models import Candidate

# Create your views here.

def adminTableView(request):
    instances = Candidate.objects.all().order_by('-timeStamp')
    return render(request, 'admin/table.html',{'instances':instances})
