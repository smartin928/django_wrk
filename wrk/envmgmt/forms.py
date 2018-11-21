from django import forms
from .models import EnvDtl, Project


class PrjForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('project_name',)
        labels = {
            'project_name': 'Project Name',
        }


class EnvDtlForm(forms.ModelForm):

    class Meta:
        model = EnvDtl
        fields = (
            'env_tier',
            'app_product',
            'app_server1',
            'app_server2',
            'app_os',
            'app_cluster',
            'app_port',
            'refs_url',
            'db_name',
            'db_server1',
            'db_server2',
            'db_type',
            'db_os',
        )
        labels = {
            'env_tier': 'Project Group',
            'app_product': 'Product',
            'app_server1': 'Primary App Server',
            'app_server2': 'Secondary App Server',
            'app_os': 'App Server O/S',
            'app_cluster': 'Clustered?',
            'refs_url': 'REFS URL',
            'db_name': 'Database Name',
            'db_server1': 'Primary DB Server',
            'db_server2': 'Secondary DB Server',
            'db_type': 'Database Type',
            'db_os': 'Database Server O/S',
        }