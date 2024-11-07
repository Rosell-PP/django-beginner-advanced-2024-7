from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home),
    path("get", views.get),
    path("delete", views.delete),
    path("update", views.update),
]