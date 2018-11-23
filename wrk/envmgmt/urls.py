from django.urls import path
from .views import index, add_details, add_prj, show_prj, add_hdr

urlpatterns = [
    path('', index),
    path('addprj/', add_prj),
    path('adddtl/', add_details),
    path('project/<int:prj_id>/', show_prj),
    path('addhdr/', add_hdr),
]