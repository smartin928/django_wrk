from django.urls import path
from .views import index, add_details, add_prj

urlpatterns = [
    path('', index),
    path('addprj/', add_prj),
    path('adddtl/', add_details),
]