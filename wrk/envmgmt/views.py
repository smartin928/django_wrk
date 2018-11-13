from django.shortcuts import render
from .forms import EnvDtlForm
from .models import Project


def index(request):
    prjs = Project.objects.values('project_name')
    return render(request, 'envmgmt/index.html', {'prjs': prjs})


#def add_project(request):
#    if request.method == 'POST':
#        form = EnvMainForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return render(request, 'envmgmt/thanks.html')
#    else:
#        form = EnvMainForm()
#
#    return render(request, 'envmgmt/addprj.html', {'form': form})


def add_details(request):
    if request.method == 'POST':
        form = EnvDtlForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'envmgmt/thanks.html')
    else:
        form = EnvDtlForm()

    return render(request, 'envmgmt/adddtl.html', {'form': form})

