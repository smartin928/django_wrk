from django.shortcuts import render
from .forms import EnvDtlForm, PrjForm, EnvHdrForm
from .models import Project, EnvHdr, EnvDtl


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


def add_hdr(request):
    if request.method == 'POST':
        form = EnvHdrForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'envmgmt/thanks.html')
    else:
        form = EnvHdrForm()
    return render(request, 'envmgmt/addhdr.html', {'form': form})


def show_prj(request, prj_name):
    prj = Project.objects.get(project_name=prj_name)
    try:
        prjdtls = EnvHdr.objects.filter(project_name_id=prj.prg_id)
    except EnvHdr.DoesNotExist:
        prjdtls = None
    return render(request, 'envmgmt/prjmain.html', {'prjdtls': prjdtls, 'prj': prj})


def show_prj_dtls(request, prj_name, dtl_id):
    try:
        dtls = EnvDtl.objects.get(env_tier_id=dtl_id)
    except EnvDtl.DoesNotExist:
        dtls = None
    return render(request, 'envmgmt/prjdtl.html', {'dtls': dtls, 'prj_name': prj_name})

