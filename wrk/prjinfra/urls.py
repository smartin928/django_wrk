from django.urls import path
from .views import index, prj_view


urlpatterns = [
    path('', index),
    path('project/<str:prj_name>', prj_view),
]