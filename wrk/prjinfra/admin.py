from django.contrib import admin
from .models import Project, Server, Rollout, RolloutDtls, RolloutTrans, Application, Database

# List of models to register
prjinfraModels = [
    Project,
    Server,
    Rollout,
    RolloutDtls,
    RolloutTrans,
    Application,
    Database,
]


# Register models from list
admin.site.register(prjinfraModels)