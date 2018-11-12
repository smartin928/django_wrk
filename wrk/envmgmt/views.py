from django.shortcuts import render
from .forms import EnvMainForm, EnvDtlForm
from .models import EnvMain


def index(request):
    prjs = EnvMain.objects.values('project_name').distinct()
    return render(request, 'envmgmt/index.html', {'prjs': prjs})


def add_project(request):
    if request.method == 'POST':
        form = EnvMainForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'envmgmt/thanks.html')
    else:
        form = EnvMainForm()
        form_typ = "Project"

    return render(request, 'envmgmt/addprj.html', {'form': form, 'form_typ': form_typ})


def add_details(request):
    if request.method == 'POST':
        form = EnvDtlForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'envmgmt/thanks.html')
    else:
        form = EnvDtlForm()
        form_typ = "Project Detail"

    return render(request, 'envmgmt/addprj.html', {'form': form, 'form_typ': form_typ})
