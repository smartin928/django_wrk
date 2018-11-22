from django.shortcuts import render
from .forms import EnvDtlForm, PrjForm
from .models import Project


def index(request):
    prjs = Project.objects.all()
    return render(request, 'envmgmt/index.html', {'prjs': prjs})


def add_prj(request):
    if request.method == 'POST':
        form = PrjForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'envmgmt/thanks.html')
    else:
        form = PrjForm()
    return render(request, 'envmgmt/addprj.html', {'form': form})


def add_details(request):
    if request.method == 'POST':
        form = EnvDtlForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'envmgmt/thanks.html')
    else:
        form = EnvDtlForm()

    return render(request, 'envmgmt/adddtl.html', {'form': form})


def show_prj(request, prj_id):
    prj = prj_id
    
    return render(request, 'envmgmt/prjmain.html', {'prj': prj})

