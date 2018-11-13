from django.contrib import admin
from .models import Project, EnvHdr, EnvDtl

admin.site.register(EnvHdr)
admin.site.register(Project)
admin.site.register(EnvDtl)