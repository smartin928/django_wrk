from django.urls import path
from .views import index, add_details

urlpatterns = [
    path('', index),
    #path('addprj/', add_project),
    path('adddtl/', add_details),
]