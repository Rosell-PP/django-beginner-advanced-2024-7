from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm

urlpatterns = [
    path("register", views.register, name='accounts-register'),
    # path("login", views.auth_login, name='accounts-login'),
    path(
        "login",
        LoginView.as_view(
            template_name="accounts/login.html",
            authentication_form=LoginForm,
            redirect_authenticated_user=True
        ),
        name='accounts-login'
    ),
    # path("logout", views.auth_logout, name='accounts-logout'),
    path("logout", LogoutView.as_view(), name='accounts-logout'),
]