from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):
    # for check if user is authenticated
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('posts-home')) 
    else:
        if request.method == "POST":
            form =  RegisterForm(request.POST)
            if form.is_valid(): 
                form.save()
                return HttpResponseRedirect(reverse('posts-home'))
        else:
            form = RegisterForm()
        
        return render(request=request, template_name="accounts/register.html", context={"form":form})

def auth_login(request):
    # for check if user is authenticated
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('posts-home')) 
    else:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]

                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse('posts-home'))
        else:
            form = LoginForm()

        return render(request, "accounts/login.html", {"form":form})
    
def auth_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('posts-home')) 
