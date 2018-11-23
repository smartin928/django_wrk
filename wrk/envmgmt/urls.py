from django.urls import path
from .views import index, add_details, add_prj, show_prj, add_hdr, show_prj_dtls

urlpatterns = [
    path('', index),
    path('addprj/', add_prj),
    path('adddtl/', add_details),
    path('project/<str:prj_name>/', show_prj),
    path('project/<str:prj_name>/<int:dtl_id>/', show_prj_dtls),
    path('addhdr/', add_hdr),
]