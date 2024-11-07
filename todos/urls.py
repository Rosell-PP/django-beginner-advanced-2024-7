from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    # path("", views.HomeClass.as_view(), name='todos-home'),
    path("", views.IndexView.as_view(), name='todos-home'),
    path("add/", views.AddClass.as_view(), name='todos-add'),
    path("create/", views.CreateTodoCreateView.as_view(), name='todos-create'),
    path("update/<int:pk>", views.UpdateTodoView.as_view(), name='todos-update'),
    path("delete/<int:pk>", views.DeleteTodoView.as_view(), name='todos-delete'),
    path("formadd/", views.AddTodoFormView.as_view(), name='todos-add-form'),
    path("simpleabout/", TemplateView.as_view(template_name="todos/about.html"), name='todos-simple-about'),
    path("about/", views.AboutView.as_view(), name='todos-about'),
    path("about/<str:name>", views.AboutView.as_view(), name='todos-params-about'),
    path("redirect/", views.AboutRedirectView.as_view(), name='todos-redirect'),
    path("detail/<int:pk>", views.DetailsTodoView.as_view(), name='todos-details'),
]