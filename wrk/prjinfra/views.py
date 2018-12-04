from django.shortcuts import render
from .models import Project, Application


def index(request):

    try:
        prjs = Project.objects.all()
    except Project.DoesNotExist:
        prjs = None

    return render(request, 'prjinfra/index.html', {'prjs': prjs})


def prj_view(request, prj_name):

    try:
        tiers = Application.objects.filter(prj__prj_name=prj_name).values('tier').distinct()
        apps = Application.objects.filter(prj__prj_name=prj_name)
    except Application.DoesNotExist:
        tiers = None
        apps = None

    return render(request, 'prjinfra/prj_view.html', {'tiers': tiers, 'apps': apps})