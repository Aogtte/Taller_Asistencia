from django.urls import path
from .import views

urlpatterns = [
    path("", views.listado),
    path("crear/", views.crear),
]