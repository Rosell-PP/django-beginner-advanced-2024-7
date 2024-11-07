from django.urls import path
from . import views

urlpatterns = [
    path("upload", views.uploadFile, name='file-upload'),
    path("server", views.server, name='file-server')
]